"""DSA demos must agree with their educational copy and published traces."""
import importlib.util
import contextlib
import io
import json
import pathlib
import subprocess
import sys
import unittest

ROOT=pathlib.Path(__file__).resolve().parents[1]
EP=ROOT/'episodes'
SLUGS=['021-two-sum','022-binary-search','023-two-pointers','024-sliding-window',
       '025-valid-parentheses','026-reverse-linked-list','027-recursion-stack',
       '028-merge-sort','029-bfs-vs-dfs','030-dp-memoization']

def load(slug):
    path=EP/slug/'demo.py'
    spec=importlib.util.spec_from_file_location('lesson_'+slug.replace('-','_'), path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

class LessonTests(unittest.TestCase):
    def test_all_demos_and_trace_fixtures_match_executions(self):
        for slug in SLUGS:
            with self.subTest(slug=slug):
                demo=load(slug)
                output=subprocess.run([sys.executable, str(EP/slug/'demo.py')],
                                      capture_output=True,text=True,check=True)
                self.assertTrue(output.stdout.strip())
                self.assertFalse(output.stderr.strip())
                fixture=json.loads((EP/slug/'trace.json').read_text(encoding='utf-8'))
                with contextlib.redirect_stdout(io.StringIO()):
                    actual = demo.main()
                self.assertEqual(actual,fixture)
                self.assertTrue((EP/slug/'README.md').exists())
                self.assertNotIn('https://youtube.com/shorts/',(EP/slug/'README.md').read_text())

    def test_two_sum_distinct_indices_and_not_found(self):
        m=load(SLUGS[0]);self.assertEqual(m.two_sum([3,3],6),(0,1))
        self.assertIsNone(m.two_sum([2],4));self.assertIsNone(m.two_sum([],5))
        self.assertEqual(m.two_sum([2,2,2],4),(0,1))

    def test_binary_search_empty_missing_and_duplicates(self):
        m=load(SLUGS[1]);self.assertEqual(m.binary_search([],1),-1)
        self.assertEqual(m.binary_search([2,4,6,8,10,12,14],12),5)
        self.assertEqual(m.binary_search([2,4,6,8,10,12,14],11),-1)
        self.assertIn(m.binary_search([1,1,1],1),[0,1,2])

    def test_sorted_two_pointers(self):
        m=load(SLUGS[2]);self.assertEqual(m.two_pointers([1,2,4,6,9],8),(1,3))
        self.assertIsNone(m.two_pointers([1,2,4],20));self.assertIsNone(m.two_pointers([5],10))
        self.assertEqual(m.two_pointers([2,2],4),(0,1))

    def test_window_negative_numbers_and_bad_width(self):
        m=load(SLUGS[3]);self.assertEqual(m.best_window([2,1,5,1,3,2],3),(9,2))
        self.assertEqual(m.best_window([-8,-4,-9],2),(-12,0))
        self.assertEqual(m.best_window([9],1),(9,0))
        for width in [0,-1,4]:
            with self.assertRaises(ValueError):m.best_window([1,2,3],width)

    def test_stack_order_and_invalid_inputs(self):
        m=load(SLUGS[4]);self.assertTrue(m.valid_brackets(''))
        self.assertTrue(m.valid_brackets('{[()]}'))
        self.assertFalse(m.valid_brackets('([)]'))
        self.assertFalse(m.valid_brackets('(()'))
        self.assertFalse(m.valid_brackets(')'))
        with self.assertRaises(ValueError):m.valid_brackets('a')

    def test_linked_list_empty_single_and_no_node_loss(self):
        m=load(SLUGS[5]);self.assertIsNone(m.reverse_list(None))
        single=m.make_list([5]);self.assertIs(m.reverse_list(single),single)
        nodes=m.make_list([1,2,3]);a,b,c=nodes,nodes.next,nodes.next.next
        result=m.reverse_list(nodes)
        self.assertIs(result,c);self.assertIs(result.next,b);self.assertIs(b.next,a)
        self.assertIsNone(a.next);self.assertEqual(m.to_values(result),[3,2,1])

    def test_factorial_base_negative_trace(self):
        m=load(SLUGS[6]);self.assertEqual(m.factorial(0),1)
        self.assertEqual(m.factorial(1),1);self.assertEqual(m.factorial(5),120)
        with self.assertRaises(ValueError):m.factorial(-1)
        events=[];m.factorial(4,events)
        self.assertEqual([e['step'] for e in events].count('return'),3)

    def test_mergesort_duplicates_input_preserved_and_stable(self):
        m=load(SLUGS[7]);v=[7,2,5,1];out=m.merge_sort(v)
        self.assertEqual(v,[7,2,5,1]);self.assertEqual(out,[1,2,5,7])
        self.assertEqual(m.merge_sort([]),[]);self.assertEqual(m.merge_sort([1]),[1])
        self.assertEqual(m.merge_sort([3,1,3,2]),[1,2,3,3])

    def test_graph_traversals_cycle_and_disconnected(self):
        m=load(SLUGS[8]);graph={'A':['B','C'],'B':['D'],'C':['E'],'D':[],'E':[]}
        self.assertEqual(m.bfs(graph,'A'),['A','B','C','D','E'])
        self.assertEqual(m.dfs(graph,'A'),['A','B','D','C','E'])
        graph['E']=['A'];graph['Z']=[]
        self.assertEqual(len(m.bfs(graph,'A')),5)
        self.assertEqual(len(m.dfs(graph,'A')),5)
        with self.assertRaises(KeyError):m.bfs(graph,'X')

    def test_memoization_caches_repeated_subproblems(self):
        m=load(SLUGS[9]);self.assertEqual(m.fibonacci(0),0)
        self.assertEqual(m.fibonacci(1),1)
        self.assertEqual(m.fibonacci(6),8)
        self.assertEqual(m.fibonacci(7),13)
        with self.assertRaises(ValueError):m.fibonacci(-1)
        events=[];m.fibonacci(6,events)
        computed={e['n'] for e in events if e['step']=='compute'}
        self.assertEqual(computed,{2,3,4,5,6})
        self.assertTrue(any(e['step']=='cache_hit' and e['n']==3 for e in events))

if __name__ == '__main__':
    unittest.main()
