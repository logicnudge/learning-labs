"""Reader-facing lessons should execute exactly as documented."""
import json
import pathlib
import re
import subprocess
import sys
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
CATALOG=json.loads((ROOT/'catalog.json').read_text(encoding='utf-8'))
class LearnerTests(unittest.TestCase):
    def test_ten_episodes_unique(self):
        self.assertEqual(list(range(11,21)),[ep['id'] for ep in CATALOG])
        self.assertEqual(len({ep['slug'] for ep in CATALOG}),10)

    def test_all_demos_match_expected_output(self):
        for ep in CATALOG:
            with self.subTest(episode=ep['id']):
                lesson=ROOT/'episodes'/f"{ep['id']:03d}-{ep['slug']}"
                self.assertTrue((lesson/'README.md').exists())
                run=subprocess.run([sys.executable,'-I','-B',str(lesson/'demo.py')],capture_output=True,text=True,timeout=5)
                self.assertEqual(run.returncode,0,run.stderr)
                self.assertEqual(run.stderr,'')
                self.assertEqual(run.stdout,ep['expected'])

    def test_educational_completeness(self):
        for ep in CATALOG:
            with self.subTest(episode=ep['id']):
                for name in ('title','learning_goal','quiz','answer','transfer','caveat','source'):
                    self.assertTrue(ep[name].strip())
                self.assertIn(ep['expected'].strip(),(ROOT/'episodes'/f"{ep['id']:03d}-{ep['slug']}"/'README.md').read_text())

    def test_public_catalog_no_user_paths_or_tokens(self):
        content=(ROOT/'catalog.json').read_text()
        for pattern in [r'[A-Za-z]:\\Users\\[^\\]+',r'/home/[^/]+/',r'(?i)authorization\s*:\s*bearer',r'[\w.+-]+@(?:gmail|outlook|yahoo)\.com']:
            self.assertIsNone(re.search(pattern,content),pattern)

if __name__=='__main__':unittest.main()
