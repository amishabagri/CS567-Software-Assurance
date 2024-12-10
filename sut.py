from __future__ import print_function
try:
    from importlib import reload
except ImportError:
    try:
        from imp import reload
    except ImportError:
        pass
import copy
import traceback
import inspect
import re
import sys
import time
import glob
import struct
import random
import subprocess
import os.path
from itertools import chain, combinations
import coverage
# BEGIN STANDALONE CODE
# END STANDALONE CODE
class sut(object):
    def act0(self):
        '''
        from collections import defaultdict
        '''
        self.__test.append(('''from collections import defaultdict ''',self.guard0,self.act0))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''from collections import defaultdict '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            from collections import defaultdict
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard0(self):
        return True
    
    def act1(self):
        '''
        class WeightedGraph:
        '''
        self.__test.append(('''class WeightedGraph: ''',self.guard1,self.act1))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class WeightedGraph: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class WeightedGraph:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard1(self):
        return True
    
    def act2(self):
        '''
        def __init__(self, vertices):
        '''
        self.__test.append(('''def __init__(self, vertices): ''',self.guard2,self.act2))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self, vertices): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self, vertices):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard2(self):
        return True
    
    def act3(self):
        '''
        self.vertices = vertices
        '''
        self.__test.append(('''self.vertices = vertices ''',self.guard3,self.act3))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.vertices = vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.vertices = vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard3(self):
        return True
    
    def act4(self):
        '''
        self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph
        '''
        self.__test.append(('''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph ''',self.guard4,self.act4))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard4(self):
        return True
    
    def act5(self):
        '''
        self.edges = []  # List to store the edges (u, v, weight)
        '''
        self.__test.append(('''self.edges = []  # List to store the edges (u, v, weight) ''',self.guard5,self.act5))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.edges = []  # List to store the edges (u, v, weight) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.edges = []  # List to store the edges (u, v, weight)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard5(self):
        return True
    
    def act6(self):
        '''
        def add_edge(self, u, v, weight):
        '''
        self.__test.append(('''def add_edge(self, u, v, weight): ''',self.guard6,self.act6))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def add_edge(self, u, v, weight): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def add_edge(self, u, v, weight):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard6(self):
        return True
    
    def act7(self):
        '''
        """Add a single edge to the graph."""
        '''
        self.__test.append(('''"""Add a single edge to the graph.""" ''',self.guard7,self.act7))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Add a single edge to the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Add a single edge to the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard7(self):
        return True
    
    def act8(self):
        '''
        if (u, v, weight) not in self.edges:
        '''
        self.__test.append(('''if (u, v, weight) not in self.edges: ''',self.guard8,self.act8))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if (u, v, weight) not in self.edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if (u, v, weight) not in self.edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard8(self):
        return True
    
    def act9(self):
        '''
        self.edges.append((u, v, weight))
        '''
        self.__test.append(('''self.edges.append((u, v, weight)) ''',self.guard9,self.act9))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.edges.append((u, v, weight)) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.edges.append((u, v, weight))
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard9(self):
        return True
    
    def act10(self):
        '''
        self.adj_list[u].append((v, weight))
        '''
        self.__test.append(('''self.adj_list[u].append((v, weight)) ''',self.guard10,self.act10))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.adj_list[u].append((v, weight)) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.adj_list[u].append((v, weight))
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard10(self):
        return True
    
    def act11(self):
        '''
        def add_multiple_edges(self, edges):
        '''
        self.__test.append(('''def add_multiple_edges(self, edges): ''',self.guard11,self.act11))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def add_multiple_edges(self, edges): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def add_multiple_edges(self, edges):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard11(self):
        return True
    
    def act12(self):
        '''
        """Add multiple edges at once."""
        '''
        self.__test.append(('''"""Add multiple edges at once.""" ''',self.guard12,self.act12))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Add multiple edges at once.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Add multiple edges at once."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard12(self):
        return True
    
    def act13(self):
        '''
        for u, v, weight in edges:
        '''
        self.__test.append(('''for u, v, weight in edges: ''',self.guard13,self.act13))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard13(self):
        return True
    
    def act14(self):
        '''
        self.add_edge(u, v, weight)
        '''
        self.__test.append(('''self.add_edge(u, v, weight) ''',self.guard14,self.act14))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.add_edge(u, v, weight) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.add_edge(u, v, weight)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard14(self):
        return True
    
    def act15(self):
        '''
        def get_edges(self):
        '''
        self.__test.append(('''def get_edges(self): ''',self.guard15,self.act15))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def get_edges(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def get_edges(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard15(self):
        return True
    
    def act16(self):
        '''
        """Return all edges in the graph."""
        '''
        self.__test.append(('''"""Return all edges in the graph.""" ''',self.guard16,self.act16))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Return all edges in the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Return all edges in the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard16(self):
        return True
    
    def act17(self):
        '''
        return self.edges
        '''
        self.__test.append(('''return self.edges ''',self.guard17,self.act17))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return self.edges '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return self.edges
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard17(self):
        return True
    
    def act18(self):
        '''
        def print_edges(self):
        '''
        self.__test.append(('''def print_edges(self): ''',self.guard18,self.act18))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def print_edges(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def print_edges(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard18(self):
        return True
    
    def act19(self):
        '''
        """Print the edges of the graph."""
        '''
        self.__test.append(('''"""Print the edges of the graph.""" ''',self.guard19,self.act19))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Print the edges of the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Print the edges of the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard19(self):
        return True
    
    def act20(self):
        '''
        print("Edges in the graph:")
        '''
        self.__test.append(('''print("Edges in the graph:") ''',self.guard20,self.act20))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("Edges in the graph:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("Edges in the graph:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard20(self):
        return True
    
    def act21(self):
        '''
        for u, v, weight in self.edges:
        '''
        self.__test.append(('''for u, v, weight in self.edges: ''',self.guard21,self.act21))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in self.edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in self.edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard21(self):
        return True
    
    def act22(self):
        '''
        {v} (Weight: {weight})")
        '''
        self.__test.append(('''{v} (Weight: {weight})") ''',self.guard22,self.act22))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''{v} (Weight: {weight})") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            {v} (Weight: {weight})
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard22(self):
        '''
        print(f"{u}
        '''
        return (print(f"{u}"))
    
    def act23(self):
        '''
        def print_adj_list(self):
        '''
        self.__test.append(('''def print_adj_list(self): ''',self.guard23,self.act23))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def print_adj_list(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def print_adj_list(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard23(self):
        return True
    
    def act24(self):
        '''
        """Print the adjacency list of the graph."""
        '''
        self.__test.append(('''"""Print the adjacency list of the graph.""" ''',self.guard24,self.act24))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Print the adjacency list of the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Print the adjacency list of the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard24(self):
        return True
    
    def act25(self):
        '''
        print("Adjacency List of the graph:")
        '''
        self.__test.append(('''print("Adjacency List of the graph:") ''',self.guard25,self.act25))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("Adjacency List of the graph:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("Adjacency List of the graph:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard25(self):
        return True
    
    def act26(self):
        '''
        for u in self.adj_list:
        '''
        self.__test.append(('''for u in self.adj_list: ''',self.guard26,self.act26))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u in self.adj_list: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u in self.adj_list:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard26(self):
        return True
    
    def act27(self):
        '''
        {self.adj_list[u]}")
        '''
        self.__test.append(('''{self.adj_list[u]}") ''',self.guard27,self.act27))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''{self.adj_list[u]}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            {self.adj_list[u]}
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard27(self):
        '''
        print(f"{u}
        '''
        return (print(f"{u}"))
    
    def act28(self):
        '''
        def is_cyclic_directed(self):
        '''
        self.__test.append(('''def is_cyclic_directed(self): ''',self.guard28,self.act28))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def is_cyclic_directed(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def is_cyclic_directed(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard28(self):
        return True
    
    def act29(self):
        '''
        """Detect if there is a cycle in a directed graph using DFS."""
        '''
        self.__test.append(('''"""Detect if there is a cycle in a directed graph using DFS.""" ''',self.guard29,self.act29))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Detect if there is a cycle in a directed graph using DFS.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Detect if there is a cycle in a directed graph using DFS."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard29(self):
        return True
    
    def act30(self):
        '''
        visited = [False] * self.vertices
        '''
        self.__test.append(('''visited = [False] * self.vertices ''',self.guard30,self.act30))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''visited = [False] * self.vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            visited = [False] * self.vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard30(self):
        return True
    
    def act31(self):
        '''
        rec_stack = [False] * self.vertices
        '''
        self.__test.append(('''rec_stack = [False] * self.vertices ''',self.guard31,self.act31))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''rec_stack = [False] * self.vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            rec_stack = [False] * self.vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard31(self):
        return True
    
    def act32(self):
        '''
        def dfs(v):
        '''
        self.__test.append(('''def dfs(v): ''',self.guard32,self.act32))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def dfs(v): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def dfs(v):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard32(self):
        return True
    
    def act33(self):
        '''
        visited[v] = True
        '''
        self.__test.append(('''visited[v] = True ''',self.guard33,self.act33))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''visited[v] = True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            visited[v] = True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard33(self):
        return True
    
    def act34(self):
        '''
        rec_stack[v] = True
        '''
        self.__test.append(('''rec_stack[v] = True ''',self.guard34,self.act34))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''rec_stack[v] = True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            rec_stack[v] = True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard34(self):
        return True
    
    def act35(self):
        '''
        for neighbor, _ in self.adj_list[v]:
        '''
        self.__test.append(('''for neighbor, _ in self.adj_list[v]: ''',self.guard35,self.act35))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for neighbor, _ in self.adj_list[v]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for neighbor, _ in self.adj_list[v]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard35(self):
        return True
    
    def act36(self):
        '''
        if not visited[neighbor] and dfs(neighbor):
        '''
        self.__test.append(('''if not visited[neighbor] and dfs(neighbor): ''',self.guard36,self.act36))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if not visited[neighbor] and dfs(neighbor): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if not visited[neighbor] and dfs(neighbor):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard36(self):
        return True
    
    def act37(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard37,self.act37))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard37(self):
        return True
    
    def act38(self):
        '''
        elif rec_stack[neighbor]:
        '''
        self.__test.append(('''elif rec_stack[neighbor]: ''',self.guard38,self.act38))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''elif rec_stack[neighbor]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            elif rec_stack[neighbor]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard38(self):
        return True
    
    def act39(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard39,self.act39))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard39(self):
        return True
    
    def act40(self):
        '''
        rec_stack[v] = False
        '''
        self.__test.append(('''rec_stack[v] = False ''',self.guard40,self.act40))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''rec_stack[v] = False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            rec_stack[v] = False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard40(self):
        return True
    
    def act41(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard41,self.act41))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard41(self):
        return True
    
    def act42(self):
        '''
        for node in range(self.vertices):
        '''
        self.__test.append(('''for node in range(self.vertices): ''',self.guard42,self.act42))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for node in range(self.vertices): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for node in range(self.vertices):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard42(self):
        return True
    
    def act43(self):
        '''
        if not visited[node]:
        '''
        self.__test.append(('''if not visited[node]: ''',self.guard43,self.act43))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if not visited[node]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if not visited[node]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard43(self):
        return True
    
    def act44(self):
        '''
        if dfs(node):
        '''
        self.__test.append(('''if dfs(node): ''',self.guard44,self.act44))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if dfs(node): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if dfs(node):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard44(self):
        return True
    
    def act45(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard45,self.act45))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard45(self):
        return True
    
    def act46(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard46,self.act46))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard46(self):
        return True
    
    def act47(self):
        '''
        def is_cyclic_undirected(self):
        '''
        self.__test.append(('''def is_cyclic_undirected(self): ''',self.guard47,self.act47))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def is_cyclic_undirected(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def is_cyclic_undirected(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard47(self):
        return True
    
    def act48(self):
        '''
        """Detect if there is a cycle in an undirected graph using DFS."""
        '''
        self.__test.append(('''"""Detect if there is a cycle in an undirected graph using DFS.""" ''',self.guard48,self.act48))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Detect if there is a cycle in an undirected graph using DFS.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Detect if there is a cycle in an undirected graph using DFS."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard48(self):
        return True
    
    def act49(self):
        '''
        visited = [False] * self.vertices
        '''
        self.__test.append(('''visited = [False] * self.vertices ''',self.guard49,self.act49))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''visited = [False] * self.vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            visited = [False] * self.vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard49(self):
        return True
    
    def act50(self):
        '''
        def dfs(v, parent):
        '''
        self.__test.append(('''def dfs(v, parent): ''',self.guard50,self.act50))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def dfs(v, parent): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def dfs(v, parent):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard50(self):
        return True
    
    def act51(self):
        '''
        visited[v] = True
        '''
        self.__test.append(('''visited[v] = True ''',self.guard51,self.act51))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''visited[v] = True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            visited[v] = True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard51(self):
        return True
    
    def act52(self):
        '''
        for neighbor, _ in self.adj_list[v]:
        '''
        self.__test.append(('''for neighbor, _ in self.adj_list[v]: ''',self.guard52,self.act52))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for neighbor, _ in self.adj_list[v]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for neighbor, _ in self.adj_list[v]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard52(self):
        return True
    
    def act53(self):
        '''
        if not visited[neighbor]:
        '''
        self.__test.append(('''if not visited[neighbor]: ''',self.guard53,self.act53))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if not visited[neighbor]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if not visited[neighbor]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard53(self):
        return True
    
    def act54(self):
        '''
        if dfs(neighbor, v):
        '''
        self.__test.append(('''if dfs(neighbor, v): ''',self.guard54,self.act54))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if dfs(neighbor, v): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if dfs(neighbor, v):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard54(self):
        return True
    
    def act55(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard55,self.act55))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard55(self):
        return True
    
    def act56(self):
        '''
        elif parent != neighbor:
        '''
        self.__test.append(('''elif parent != neighbor: ''',self.guard56,self.act56))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''elif parent != neighbor: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            elif parent != neighbor:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard56(self):
        return True
    
    def act57(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard57,self.act57))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard57(self):
        return True
    
    def act58(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard58,self.act58))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard58(self):
        return True
    
    def act59(self):
        '''
        for node in range(self.vertices):
        '''
        self.__test.append(('''for node in range(self.vertices): ''',self.guard59,self.act59))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for node in range(self.vertices): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for node in range(self.vertices):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard59(self):
        return True
    
    def act60(self):
        '''
        if not visited[node]:
        '''
        self.__test.append(('''if not visited[node]: ''',self.guard60,self.act60))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if not visited[node]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if not visited[node]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard60(self):
        return True
    
    def act61(self):
        '''
        if dfs(node, -1):
        '''
        self.__test.append(('''if dfs(node, -1): ''',self.guard61,self.act61))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if dfs(node, -1): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if dfs(node, -1):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard61(self):
        return True
    
    def act62(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard62,self.act62))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard62(self):
        return True
    
    def act63(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard63,self.act63))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard63(self):
        return True
    
    def act64(self):
        '''
        def is_negative_cycle(self):
        '''
        self.__test.append(('''def is_negative_cycle(self): ''',self.guard64,self.act64))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def is_negative_cycle(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def is_negative_cycle(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard64(self):
        return True
    
    def act65(self):
        '''
        """Detect if there is a negative cycle using Bellman-Ford."""
        '''
        self.__test.append(('''"""Detect if there is a negative cycle using Bellman-Ford.""" ''',self.guard65,self.act65))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Detect if there is a negative cycle using Bellman-Ford.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Detect if there is a negative cycle using Bellman-Ford."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard65(self):
        return True
    
    def act66(self):
        '''
        dist = [float("inf")] * self.vertices
        '''
        self.__test.append(('''dist = [float("inf")] * self.vertices ''',self.guard66,self.act66))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''dist = [float("inf")] * self.vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            dist = [float("inf")] * self.vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard66(self):
        return True
    
    def act67(self):
        '''
        dist[0] = 0  # Start from node 0
        '''
        self.__test.append(('''dist[0] = 0  # Start from node 0 ''',self.guard67,self.act67))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''dist[0] = 0  # Start from node 0 '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            dist[0] = 0  # Start from node 0
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard67(self):
        return True
    
    def act68(self):
        '''
        for _ in range(self.vertices - 1):
        '''
        self.__test.append(('''for _ in range(self.vertices - 1): ''',self.guard68,self.act68))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for _ in range(self.vertices - 1): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for _ in range(self.vertices - 1):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard68(self):
        return True
    
    def act69(self):
        '''
        for u, v, weight in self.edges:
        '''
        self.__test.append(('''for u, v, weight in self.edges: ''',self.guard69,self.act69))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in self.edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in self.edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard69(self):
        return True
    
    def act70(self):
        '''
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        '''
        self.__test.append(('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard70,self.act70))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard70(self):
        return True
    
    def act71(self):
        '''
        dist[v] = dist[u] + weight
        '''
        self.__test.append(('''dist[v] = dist[u] + weight ''',self.guard71,self.act71))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''dist[v] = dist[u] + weight '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            dist[v] = dist[u] + weight
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard71(self):
        return True
    
    def act72(self):
        '''
        for u, v, weight in self.edges:
        '''
        self.__test.append(('''for u, v, weight in self.edges: ''',self.guard72,self.act72))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in self.edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in self.edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard72(self):
        return True
    
    def act73(self):
        '''
        if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        '''
        self.__test.append(('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard73,self.act73))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if dist[u] != float("inf") and dist[u] + weight < dist[v]:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard73(self):
        return True
    
    def act74(self):
        '''
        return True  # Negative cycle detected
        '''
        self.__test.append(('''return True  # Negative cycle detected ''',self.guard74,self.act74))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True  # Negative cycle detected '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True  # Negative cycle detected
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard74(self):
        return True
    
    def act75(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard75,self.act75))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard75(self):
        return True
    
    def act76(self):
        '''
        def reset_graph(self):
        '''
        self.__test.append(('''def reset_graph(self): ''',self.guard76,self.act76))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def reset_graph(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def reset_graph(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard76(self):
        return True
    
    def act77(self):
        '''
        """Reset the graph to its empty state."""
        '''
        self.__test.append(('''"""Reset the graph to its empty state.""" ''',self.guard77,self.act77))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Reset the graph to its empty state.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Reset the graph to its empty state."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard77(self):
        return True
    
    def act78(self):
        '''
        self.edges = []  # Clear all edges
        '''
        self.__test.append(('''self.edges = []  # Clear all edges ''',self.guard78,self.act78))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.edges = []  # Clear all edges '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.edges = []  # Clear all edges
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard78(self):
        return True
    
    def act79(self):
        '''
        self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex
        '''
        self.__test.append(('''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex ''',self.guard79,self.act79))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard79(self):
        return True
    
    def act80(self):
        '''
        def union(self, parent, u, v):
        '''
        self.__test.append(('''def union(self, parent, u, v): ''',self.guard80,self.act80))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def union(self, parent, u, v): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def union(self, parent, u, v):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard80(self):
        return True
    
    def act81(self):
        '''
        """Union-find helper function."""
        '''
        self.__test.append(('''"""Union-find helper function.""" ''',self.guard81,self.act81))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Union-find helper function.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Union-find helper function."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard81(self):
        return True
    
    def act82(self):
        '''
        root_u = self.find_parent(parent, u)
        '''
        self.__test.append(('''root_u = self.find_parent(parent, u) ''',self.guard82,self.act82))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''root_u = self.find_parent(parent, u) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            root_u = self.find_parent(parent, u)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard82(self):
        return True
    
    def act83(self):
        '''
        root_v = self.find_parent(parent, v)
        '''
        self.__test.append(('''root_v = self.find_parent(parent, v) ''',self.guard83,self.act83))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''root_v = self.find_parent(parent, v) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            root_v = self.find_parent(parent, v)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard83(self):
        return True
    
    def act84(self):
        '''
        if root_u != root_v:
        '''
        self.__test.append(('''if root_u != root_v: ''',self.guard84,self.act84))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if root_u != root_v: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if root_u != root_v:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard84(self):
        return True
    
    def act85(self):
        '''
        parent[root_u] = root_v
        '''
        self.__test.append(('''parent[root_u] = root_v ''',self.guard85,self.act85))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''parent[root_u] = root_v '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            parent[root_u] = root_v
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard85(self):
        return True
    
    def act86(self):
        '''
        def find_parent(self, parent, v):
        '''
        self.__test.append(('''def find_parent(self, parent, v): ''',self.guard86,self.act86))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def find_parent(self, parent, v): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def find_parent(self, parent, v):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard86(self):
        return True
    
    def act87(self):
        '''
        """Find the root of the node using path compression."""
        '''
        self.__test.append(('''"""Find the root of the node using path compression.""" ''',self.guard87,self.act87))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Find the root of the node using path compression.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Find the root of the node using path compression."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard87(self):
        return True
    
    def act88(self):
        '''
        if parent[v] == -1:
        '''
        self.__test.append(('''if parent[v] == -1: ''',self.guard88,self.act88))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if parent[v] == -1: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if parent[v] == -1:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard88(self):
        return True
    
    def act89(self):
        '''
        return v
        '''
        self.__test.append(('''return v ''',self.guard89,self.act89))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return v '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return v
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard89(self):
        return True
    
    def act90(self):
        '''
        parent[v] = self.find_parent(parent, parent[v])
        '''
        self.__test.append(('''parent[v] = self.find_parent(parent, parent[v]) ''',self.guard90,self.act90))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''parent[v] = self.find_parent(parent, parent[v]) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            parent[v] = self.find_parent(parent, parent[v])
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard90(self):
        return True
    
    def act91(self):
        '''
        return parent[v]
        '''
        self.__test.append(('''return parent[v] ''',self.guard91,self.act91))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return parent[v] '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return parent[v]
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard91(self):
        return True
    
    def act92(self):
        '''
        def is_cyclic_undirected_union_find(self):
        '''
        self.__test.append(('''def is_cyclic_undirected_union_find(self): ''',self.guard92,self.act92))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def is_cyclic_undirected_union_find(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def is_cyclic_undirected_union_find(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard92(self):
        return True
    
    def act93(self):
        '''
        """Detect cycles in an undirected graph using Union-Find."""
        '''
        self.__test.append(('''"""Detect cycles in an undirected graph using Union-Find.""" ''',self.guard93,self.act93))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Detect cycles in an undirected graph using Union-Find.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Detect cycles in an undirected graph using Union-Find."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard93(self):
        return True
    
    def act94(self):
        '''
        parent = [-1] * self.vertices
        '''
        self.__test.append(('''parent = [-1] * self.vertices ''',self.guard94,self.act94))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''parent = [-1] * self.vertices '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            parent = [-1] * self.vertices
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard94(self):
        return True
    
    def act95(self):
        '''
        for u, v, _ in self.edges:
        '''
        self.__test.append(('''for u, v, _ in self.edges: ''',self.guard95,self.act95))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, _ in self.edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, _ in self.edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard95(self):
        return True
    
    def act96(self):
        '''
        x = self.find_parent(parent, u)
        '''
        self.__test.append(('''x = self.find_parent(parent, u) ''',self.guard96,self.act96))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''x = self.find_parent(parent, u) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            x = self.find_parent(parent, u)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard96(self):
        return True
    
    def act97(self):
        '''
        y = self.find_parent(parent, v)
        '''
        self.__test.append(('''y = self.find_parent(parent, v) ''',self.guard97,self.act97))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''y = self.find_parent(parent, v) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            y = self.find_parent(parent, v)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard97(self):
        return True
    
    def act98(self):
        '''
        if x == y:
        '''
        self.__test.append(('''if x == y: ''',self.guard98,self.act98))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if x == y: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if x == y:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard98(self):
        return True
    
    def act99(self):
        '''
        return True
        '''
        self.__test.append(('''return True ''',self.guard99,self.act99))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return True '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return True
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard99(self):
        return True
    
    def act100(self):
        '''
        self.union(parent, x, y)
        '''
        self.__test.append(('''self.union(parent, x, y) ''',self.guard100,self.act100))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.union(parent, x, y) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.union(parent, x, y)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard100(self):
        return True
    
    def act101(self):
        '''
        return False
        '''
        self.__test.append(('''return False ''',self.guard101,self.act101))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard101(self):
        return True
    
    def act102(self):
        '''
        def reset_graph_helper(self):
        '''
        self.__test.append(('''def reset_graph_helper(self): ''',self.guard102,self.act102))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def reset_graph_helper(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def reset_graph_helper(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard102(self):
        return True
    
    def act103(self):
        '''
        """Reset the graph to an empty state for testing."""
        '''
        self.__test.append(('''"""Reset the graph to an empty state for testing.""" ''',self.guard103,self.act103))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Reset the graph to an empty state for testing.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Reset the graph to an empty state for testing."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard103(self):
        return True
    
    def act104(self):
        '''
        self.edges = []
        '''
        self.__test.append(('''self.edges = [] ''',self.guard104,self.act104))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.edges = [] '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.edges = []
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard104(self):
        return True
    
    def act105(self):
        '''
        self.adj_list = defaultdict(list)
        '''
        self.__test.append(('''self.adj_list = defaultdict(list) ''',self.guard105,self.act105))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.adj_list = defaultdict(list) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.adj_list = defaultdict(list)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard105(self):
        return True
    
    def act106(self):
        '''
        def get_edges_helper(self):
        '''
        self.__test.append(('''def get_edges_helper(self): ''',self.guard106,self.act106))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def get_edges_helper(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def get_edges_helper(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard106(self):
        return True
    
    def act107(self):
        '''
        """Return all edges for testing."""
        '''
        self.__test.append(('''"""Return all edges for testing.""" ''',self.guard107,self.act107))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Return all edges for testing.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Return all edges for testing."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard107(self):
        return True
    
    def act108(self):
        '''
        return self.edges
        '''
        self.__test.append(('''return self.edges ''',self.guard108,self.act108))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''return self.edges '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            return self.edges
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard108(self):
        return True
    
    def act109(self):
        '''
        def add_multiple_edges_helper(self, edges):
        '''
        self.__test.append(('''def add_multiple_edges_helper(self, edges): ''',self.guard109,self.act109))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def add_multiple_edges_helper(self, edges): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def add_multiple_edges_helper(self, edges):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard109(self):
        return True
    
    def act110(self):
        '''
        """Add multiple edges for testing."""
        '''
        self.__test.append(('''"""Add multiple edges for testing.""" ''',self.guard110,self.act110))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Add multiple edges for testing.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Add multiple edges for testing."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard110(self):
        return True
    
    def act111(self):
        '''
        for edge in edges:
        '''
        self.__test.append(('''for edge in edges: ''',self.guard111,self.act111))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for edge in edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for edge in edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard111(self):
        return True
    
    def act112(self):
        '''
        self.add_edge(*edge)
        '''
        self.__test.append(('''self.add_edge(*edge) ''',self.guard112,self.act112))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.add_edge(*edge) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.add_edge(*edge)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard112(self):
        return True
    
    def act113(self):
        '''
        class CycleDetectionResults:
        '''
        self.__test.append(('''class CycleDetectionResults: ''',self.guard113,self.act113))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class CycleDetectionResults: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class CycleDetectionResults:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard113(self):
        return True
    
    def act114(self):
        '''
        def __init__(self):
        '''
        self.__test.append(('''def __init__(self): ''',self.guard114,self.act114))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard114(self):
        return True
    
    def act115(self):
        '''
        self.directed_cycle_detected = False
        '''
        self.__test.append(('''self.directed_cycle_detected = False ''',self.guard115,self.act115))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.directed_cycle_detected = False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.directed_cycle_detected = False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard115(self):
        return True
    
    def act116(self):
        '''
        self.undirected_cycle_detected = False
        '''
        self.__test.append(('''self.undirected_cycle_detected = False ''',self.guard116,self.act116))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.undirected_cycle_detected = False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.undirected_cycle_detected = False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard116(self):
        return True
    
    def act117(self):
        '''
        self.negative_cycle_detected = False
        '''
        self.__test.append(('''self.negative_cycle_detected = False ''',self.guard117,self.act117))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.negative_cycle_detected = False '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.negative_cycle_detected = False
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard117(self):
        return True
    
    def act118(self):
        '''
        class GraphRenderer:
        '''
        self.__test.append(('''class GraphRenderer: ''',self.guard118,self.act118))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class GraphRenderer: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class GraphRenderer:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard118(self):
        return True
    
    def act119(self):
        '''
        def __init__(self, graph):
        '''
        self.__test.append(('''def __init__(self, graph): ''',self.guard119,self.act119))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self, graph): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self, graph):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard119(self):
        return True
    
    def act120(self):
        '''
        """Initialize the renderer for visualizing the graph."""
        '''
        self.__test.append(('''"""Initialize the renderer for visualizing the graph.""" ''',self.guard120,self.act120))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Initialize the renderer for visualizing the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Initialize the renderer for visualizing the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard120(self):
        return True
    
    def act121(self):
        '''
        self.graph = graph
        '''
        self.__test.append(('''self.graph = graph ''',self.guard121,self.act121))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph = graph '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph = graph
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard121(self):
        return True
    
    def act122(self):
        '''
        def render_edges(self):
        '''
        self.__test.append(('''def render_edges(self): ''',self.guard122,self.act122))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def render_edges(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def render_edges(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard122(self):
        return True
    
    def act123(self):
        '''
        """Render the edges of the graph."""
        '''
        self.__test.append(('''"""Render the edges of the graph.""" ''',self.guard123,self.act123))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Render the edges of the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Render the edges of the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard123(self):
        return True
    
    def act124(self):
        '''
        print("\nRendering edges of the graph:")
        '''
        self.__test.append(('''print("\nRendering edges of the graph:") ''',self.guard124,self.act124))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("\nRendering edges of the graph:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("\nRendering edges of the graph:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard124(self):
        return True
    
    def act125(self):
        '''
        for u, v, weight in self.graph.get_edges():
        '''
        self.__test.append(('''for u, v, weight in self.graph.get_edges(): ''',self.guard125,self.act125))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in self.graph.get_edges(): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in self.graph.get_edges():
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard125(self):
        return True
    
    def act126(self):
        '''
        {v} (Weight: {weight})")
        '''
        self.__test.append(('''{v} (Weight: {weight})") ''',self.guard126,self.act126))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''{v} (Weight: {weight})") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            {v} (Weight: {weight})")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard126(self):
        '''
        print(f"{u}
        '''
        return (print(f"{u})
    
    def act127(self):
        '''
        def render_adj_list(self):
        '''
        self.__test.append(('''def render_adj_list(self): ''',self.guard127,self.act127))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def render_adj_list(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def render_adj_list(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard127(self):
        return True
    
    def act128(self):
        '''
        """Render the adjacency list of the graph."""
        '''
        self.__test.append(('''"""Render the adjacency list of the graph.""" ''',self.guard128,self.act128))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Render the adjacency list of the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Render the adjacency list of the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard128(self):
        return True
    
    def act129(self):
        '''
        print("\nRendering adjacency list:")
        '''
        self.__test.append(('''print("\nRendering adjacency list:") ''',self.guard129,self.act129))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("\nRendering adjacency list:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("\nRendering adjacency list:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard129(self):
        return True
    
    def act130(self):
        '''
        self.graph.print_adj_list()
        '''
        self.__test.append(('''self.graph.print_adj_list() ''',self.guard130,self.act130))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph.print_adj_list() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph.print_adj_list()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard130(self):
        return True
    
    def act131(self):
        '''
        def render_summary(self):
        '''
        self.__test.append(('''def render_summary(self): ''',self.guard131,self.act131))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def render_summary(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def render_summary(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard131(self):
        return True
    
    def act132(self):
        '''
        """Render a summary of the graph."""
        '''
        self.__test.append(('''"""Render a summary of the graph.""" ''',self.guard132,self.act132))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Render a summary of the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Render a summary of the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard132(self):
        return True
    
    def act133(self):
        '''
        print("\nGraph summary:")
        '''
        self.__test.append(('''print("\nGraph summary:") ''',self.guard133,self.act133))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("\nGraph summary:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("\nGraph summary:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard133(self):
        return True
    
    def act134(self):
        '''
        print(f"Total vertices: {self.graph.vertices}")
        '''
        self.__test.append(('''print(f"Total vertices: {self.graph.vertices}") ''',self.guard134,self.act134))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Total vertices: {self.graph.vertices}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Total vertices: {self.graph.vertices}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard134(self):
        return True
    
    def act135(self):
        '''
        print(f"Total edges: {len(self.graph.get_edges())}")
        '''
        self.__test.append(('''print(f"Total edges: {len(self.graph.get_edges())}") ''',self.guard135,self.act135))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Total edges: {len(self.graph.get_edges())}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Total edges: {len(self.graph.get_edges())}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard135(self):
        return True
    
    def act136(self):
        '''
        print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}")
        '''
        self.__test.append(('''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") ''',self.guard136,self.act136))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard136(self):
        return True
    
    def act137(self):
        '''
        print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}")
        '''
        self.__test.append(('''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") ''',self.guard137,self.act137))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard137(self):
        return True
    
    def act138(self):
        '''
        print(f"Has negative cycle: {self.graph.is_negative_cycle()}")
        '''
        self.__test.append(('''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") ''',self.guard138,self.act138))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Has negative cycle: {self.graph.is_negative_cycle()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard138(self):
        return True
    
    def act139(self):
        '''
        import matplotlib.pyplot as plt
        '''
        self.__test.append(('''import matplotlib.pyplot as plt ''',self.guard139,self.act139))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''import matplotlib.pyplot as plt '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            import matplotlib.pyplot as plt
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard139(self):
        return True
    
    def act140(self):
        '''
        import networkx as nx
        '''
        self.__test.append(('''import networkx as nx ''',self.guard140,self.act140))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''import networkx as nx '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            import networkx as nx
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard140(self):
        return True
    
    def act141(self):
        '''
        class WeightedGraphVisualization:
        '''
        self.__test.append(('''class WeightedGraphVisualization: ''',self.guard141,self.act141))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class WeightedGraphVisualization: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class WeightedGraphVisualization:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard141(self):
        return True
    
    def act142(self):
        '''
        def __init__(self, graph):
        '''
        self.__test.append(('''def __init__(self, graph): ''',self.guard142,self.act142))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self, graph): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self, graph):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard142(self):
        return True
    
    def act143(self):
        '''
        """Initialize the visualization of weighted graph."""
        '''
        self.__test.append(('''"""Initialize the visualization of weighted graph.""" ''',self.guard143,self.act143))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Initialize the visualization of weighted graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Initialize the visualization of weighted graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard143(self):
        return True
    
    def act144(self):
        '''
        self.graph = graph
        '''
        self.__test.append(('''self.graph = graph ''',self.guard144,self.act144))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph = graph '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph = graph
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard144(self):
        return True
    
    def act145(self):
        '''
        def visualize(self):
        '''
        self.__test.append(('''def visualize(self): ''',self.guard145,self.act145))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def visualize(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def visualize(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard145(self):
        return True
    
    def act146(self):
        '''
        """Visualize the graph with weighted edges using networkx and matplotlib."""
        '''
        self.__test.append(('''"""Visualize the graph with weighted edges using networkx and matplotlib.""" ''',self.guard146,self.act146))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Visualize the graph with weighted edges using networkx and matplotlib.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Visualize the graph with weighted edges using networkx and matplotlib."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard146(self):
        return True
    
    def act147(self):
        '''
        G = nx.DiGraph()  # Using DiGraph for directed graph visualization
        '''
        self.__test.append(('''G = nx.DiGraph()  # Using DiGraph for directed graph visualization ''',self.guard147,self.act147))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            G = nx.DiGraph()  # Using DiGraph for directed graph visualization
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard147(self):
        return True
    
    def act148(self):
        '''
        for u, v, weight in self.graph.get_edges():
        '''
        self.__test.append(('''for u, v, weight in self.graph.get_edges(): ''',self.guard148,self.act148))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for u, v, weight in self.graph.get_edges(): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for u, v, weight in self.graph.get_edges():
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard148(self):
        return True
    
    def act149(self):
        '''
        G.add_edge(u, v, weight=weight)
        '''
        self.__test.append(('''G.add_edge(u, v, weight=weight) ''',self.guard149,self.act149))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''G.add_edge(u, v, weight=weight) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            G.add_edge(u, v, weight=weight)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard149(self):
        return True
    
    def act150(self):
        '''
        pos = nx.spring_layout(G)  # Layout for node positioning
        '''
        self.__test.append(('''pos = nx.spring_layout(G)  # Layout for node positioning ''',self.guard150,self.act150))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''pos = nx.spring_layout(G)  # Layout for node positioning '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            pos = nx.spring_layout(G)  # Layout for node positioning
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard150(self):
        return True
    
    def act151(self):
        '''
        edge_labels = nx.get_edge_attributes(G, 'weight')
        '''
        self.__test.append(('''edge_labels = nx.get_edge_attributes(G, 'weight') ''',self.guard151,self.act151))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''edge_labels = nx.get_edge_attributes(G, 'weight') '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            edge_labels = nx.get_edge_attributes(G, 'weight')
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard151(self):
        return True
    
    def act152(self):
        '''
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
        '''
        self.__test.append(('''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') ''',self.guard152,self.act152))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold')
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard152(self):
        return True
    
    def act153(self):
        '''
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        '''
        self.__test.append(('''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) ''',self.guard153,self.act153))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard153(self):
        return True
    
    def act154(self):
        '''
        plt.title("Graph Visualization with Weighted Edges")
        '''
        self.__test.append(('''plt.title("Graph Visualization with Weighted Edges") ''',self.guard154,self.act154))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''plt.title("Graph Visualization with Weighted Edges") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            plt.title("Graph Visualization with Weighted Edges")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard154(self):
        return True
    
    def act155(self):
        '''
        plt.show()
        '''
        self.__test.append(('''plt.show() ''',self.guard155,self.act155))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''plt.show() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            plt.show()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard155(self):
        return True
    
    def act156(self):
        '''
        class WeightedGraphHandler:
        '''
        self.__test.append(('''class WeightedGraphHandler: ''',self.guard156,self.act156))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class WeightedGraphHandler: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class WeightedGraphHandler:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard156(self):
        return True
    
    def act157(self):
        '''
        def __init__(self, vertices):
        '''
        self.__test.append(('''def __init__(self, vertices): ''',self.guard157,self.act157))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self, vertices): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self, vertices):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard157(self):
        return True
    
    def act158(self):
        '''
        """Initialize the graph handler."""
        '''
        self.__test.append(('''"""Initialize the graph handler.""" ''',self.guard158,self.act158))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Initialize the graph handler.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Initialize the graph handler."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard158(self):
        return True
    
    def act159(self):
        '''
        self.graph = WeightedGraph(vertices)
        '''
        self.__test.append(('''self.graph = WeightedGraph(vertices) ''',self.guard159,self.act159))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph = WeightedGraph(vertices) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph = WeightedGraph(vertices)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard159(self):
        return True
    
    def act160(self):
        '''
        self.renderer = GraphRenderer(self.graph)
        '''
        self.__test.append(('''self.renderer = GraphRenderer(self.graph) ''',self.guard160,self.act160))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.renderer = GraphRenderer(self.graph) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.renderer = GraphRenderer(self.graph)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard160(self):
        return True
    
    def act161(self):
        '''
        self.visualizer = WeightedGraphVisualization(self.graph)
        '''
        self.__test.append(('''self.visualizer = WeightedGraphVisualization(self.graph) ''',self.guard161,self.act161))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.visualizer = WeightedGraphVisualization(self.graph) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.visualizer = WeightedGraphVisualization(self.graph)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard161(self):
        return True
    
    def act162(self):
        '''
        def add_edges(self, edges):
        '''
        self.__test.append(('''def add_edges(self, edges): ''',self.guard162,self.act162))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def add_edges(self, edges): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def add_edges(self, edges):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard162(self):
        return True
    
    def act163(self):
        '''
        """Add edges to the graph."""
        '''
        self.__test.append(('''"""Add edges to the graph.""" ''',self.guard163,self.act163))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Add edges to the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Add edges to the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard163(self):
        return True
    
    def act164(self):
        '''
        for edge in edges:
        '''
        self.__test.append(('''for edge in edges: ''',self.guard164,self.act164))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''for edge in edges: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            for edge in edges:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard164(self):
        return True
    
    def act165(self):
        '''
        self.graph.add_edge(*edge)
        '''
        self.__test.append(('''self.graph.add_edge(*edge) ''',self.guard165,self.act165))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph.add_edge(*edge) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph.add_edge(*edge)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard165(self):
        return True
    
    def act166(self):
        '''
        def render_graph(self):
        '''
        self.__test.append(('''def render_graph(self): ''',self.guard166,self.act166))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def render_graph(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def render_graph(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard166(self):
        return True
    
    def act167(self):
        '''
        """Render the graph using the renderer."""
        '''
        self.__test.append(('''"""Render the graph using the renderer.""" ''',self.guard167,self.act167))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Render the graph using the renderer.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Render the graph using the renderer."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard167(self):
        return True
    
    def act168(self):
        '''
        self.renderer.render_edges()
        '''
        self.__test.append(('''self.renderer.render_edges() ''',self.guard168,self.act168))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.renderer.render_edges() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.renderer.render_edges()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard168(self):
        return True
    
    def act169(self):
        '''
        self.renderer.render_adj_list()
        '''
        self.__test.append(('''self.renderer.render_adj_list() ''',self.guard169,self.act169))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.renderer.render_adj_list() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.renderer.render_adj_list()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard169(self):
        return True
    
    def act170(self):
        '''
        def visualize_graph(self):
        '''
        self.__test.append(('''def visualize_graph(self): ''',self.guard170,self.act170))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def visualize_graph(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def visualize_graph(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard170(self):
        return True
    
    def act171(self):
        '''
        """Visualize the graph using the visualizer."""
        '''
        self.__test.append(('''"""Visualize the graph using the visualizer.""" ''',self.guard171,self.act171))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Visualize the graph using the visualizer.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Visualize the graph using the visualizer."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard171(self):
        return True
    
    def act172(self):
        '''
        self.visualizer.visualize()
        '''
        self.__test.append(('''self.visualizer.visualize() ''',self.guard172,self.act172))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.visualizer.visualize() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.visualizer.visualize()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard172(self):
        return True
    
    def act173(self):
        '''
        def cycle_detection_summary(self):
        '''
        self.__test.append(('''def cycle_detection_summary(self): ''',self.guard173,self.act173))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def cycle_detection_summary(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def cycle_detection_summary(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard173(self):
        return True
    
    def act174(self):
        '''
        """Print the cycle detection summary."""
        '''
        self.__test.append(('''"""Print the cycle detection summary.""" ''',self.guard174,self.act174))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Print the cycle detection summary.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Print the cycle detection summary."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard174(self):
        return True
    
    def act175(self):
        '''
        print("\nCycle detection summary:")
        '''
        self.__test.append(('''print("\nCycle detection summary:") ''',self.guard175,self.act175))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print("\nCycle detection summary:") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print("\nCycle detection summary:")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard175(self):
        return True
    
    def act176(self):
        '''
        print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}")
        '''
        self.__test.append(('''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") ''',self.guard176,self.act176))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard176(self):
        return True
    
    def act177(self):
        '''
        print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}")
        '''
        self.__test.append(('''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") ''',self.guard177,self.act177))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard177(self):
        return True
    
    def act178(self):
        '''
        print(f"Negative cycle detected: {self.graph.is_negative_cycle()}")
        '''
        self.__test.append(('''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") ''',self.guard178,self.act178))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Negative cycle detected: {self.graph.is_negative_cycle()}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard178(self):
        return True
    
    def act179(self):
        '''
        class GraphCycleAnalysis:
        '''
        self.__test.append(('''class GraphCycleAnalysis: ''',self.guard179,self.act179))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''class GraphCycleAnalysis: '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            class GraphCycleAnalysis:
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard179(self):
        return True
    
    def act180(self):
        '''
        def __init__(self, graph):
        '''
        self.__test.append(('''def __init__(self, graph): ''',self.guard180,self.act180))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def __init__(self, graph): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def __init__(self, graph):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard180(self):
        return True
    
    def act181(self):
        '''
        """Initialize cycle analysis on the graph."""
        '''
        self.__test.append(('''"""Initialize cycle analysis on the graph.""" ''',self.guard181,self.act181))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Initialize cycle analysis on the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Initialize cycle analysis on the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard181(self):
        return True
    
    def act182(self):
        '''
        self.graph = graph
        '''
        self.__test.append(('''self.graph = graph ''',self.guard182,self.act182))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.graph = graph '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.graph = graph
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard182(self):
        return True
    
    def act183(self):
        '''
        self.results = CycleDetectionResults()
        '''
        self.__test.append(('''self.results = CycleDetectionResults() ''',self.guard183,self.act183))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.results = CycleDetectionResults() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.results = CycleDetectionResults()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard183(self):
        return True
    
    def act184(self):
        '''
        def analyze_cycles(self):
        '''
        self.__test.append(('''def analyze_cycles(self): ''',self.guard184,self.act184))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def analyze_cycles(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def analyze_cycles(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard184(self):
        return True
    
    def act185(self):
        '''
        """Analyze different types of cycles in the graph."""
        '''
        self.__test.append(('''"""Analyze different types of cycles in the graph.""" ''',self.guard185,self.act185))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Analyze different types of cycles in the graph.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Analyze different types of cycles in the graph."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard185(self):
        return True
    
    def act186(self):
        '''
        self.results.directed_cycle_detected = self.graph.is_cyclic_directed()
        '''
        self.__test.append(('''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() ''',self.guard186,self.act186))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.results.directed_cycle_detected = self.graph.is_cyclic_directed()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard186(self):
        return True
    
    def act187(self):
        '''
        self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected()
        '''
        self.__test.append(('''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() ''',self.guard187,self.act187))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard187(self):
        return True
    
    def act188(self):
        '''
        self.results.negative_cycle_detected = self.graph.is_negative_cycle()
        '''
        self.__test.append(('''self.results.negative_cycle_detected = self.graph.is_negative_cycle() ''',self.guard188,self.act188))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            self.results.negative_cycle_detected = self.graph.is_negative_cycle()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard188(self):
        return True
    
    def act189(self):
        '''
        def print_analysis(self):
        '''
        self.__test.append(('''def print_analysis(self): ''',self.guard189,self.act189))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''def print_analysis(self): '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            def print_analysis(self):
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard189(self):
        return True
    
    def act190(self):
        '''
        """Print the analysis results."""
        '''
        self.__test.append(('''"""Print the analysis results.""" ''',self.guard190,self.act190))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''"""Print the analysis results.""" '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            """Print the analysis results."""
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard190(self):
        return True
    
    def act191(self):
        '''
        print(f"Directed cycle detected: {self.results.directed_cycle_detected}")
        '''
        self.__test.append(('''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") ''',self.guard191,self.act191))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Directed cycle detected: {self.results.directed_cycle_detected}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard191(self):
        return True
    
    def act192(self):
        '''
        print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}")
        '''
        self.__test.append(('''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") ''',self.guard192,self.act192))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard192(self):
        return True
    
    def act193(self):
        '''
        print(f"Negative cycle detected: {self.results.negative_cycle_detected}")
        '''
        self.__test.append(('''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") ''',self.guard193,self.act193))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            print(f"Negative cycle detected: {self.results.negative_cycle_detected}")
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard193(self):
        return True
    
    def act194(self):
        '''
        if __name__ == "__main__":
        '''
        self.__test.append(('''if __name__ == "__main__": ''',self.guard194,self.act194))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''if __name__ == "__main__": '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            if __name__ == "__main__":
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard194(self):
        return True
    
    def act195(self):
        '''
        graph_handler = WeightedGraphHandler(4)
        '''
        self.__test.append(('''graph_handler = WeightedGraphHandler(4) ''',self.guard195,self.act195))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''graph_handler = WeightedGraphHandler(4) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            graph_handler = WeightedGraphHandler(4)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard195(self):
        return True
    
    def act196(self):
        '''
        edges = [
        '''
        self.__test.append(('''edges = [ ''',self.guard196,self.act196))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''edges = [ '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            edges = [
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard196(self):
        return True
    
    def act197(self):
        '''
        (0, 1, 10),  # Edge from 0 to 1 with weight 10
        '''
        self.__test.append(('''(0, 1, 10),  # Edge from 0 to 1 with weight 10 ''',self.guard197,self.act197))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''(0, 1, 10),  # Edge from 0 to 1 with weight 10 '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            (0, 1, 10),  # Edge from 0 to 1 with weight 10
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard197(self):
        return True
    
    def act198(self):
        '''
        (1, 2, 20),  # Edge from 1 to 2 with weight 20
        '''
        self.__test.append(('''(1, 2, 20),  # Edge from 1 to 2 with weight 20 ''',self.guard198,self.act198))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''(1, 2, 20),  # Edge from 1 to 2 with weight 20 '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            (1, 2, 20),  # Edge from 1 to 2 with weight 20
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard198(self):
        return True
    
    def act199(self):
        '''
        (2, 3, 30),  # Edge from 2 to 3 with weight 30
        '''
        self.__test.append(('''(2, 3, 30),  # Edge from 2 to 3 with weight 30 ''',self.guard199,self.act199))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''(2, 3, 30),  # Edge from 2 to 3 with weight 30 '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            (2, 3, 30),  # Edge from 2 to 3 with weight 30
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard199(self):
        return True
    
    def act200(self):
        '''
        
        '''
        self.__test.append((''' ''',self.guard200,self.act200))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName(''' '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            1        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard200(self):
        '''
        (3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0
        '''
        return ((3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0)
    
    def act201(self):
        '''
        (0, 2, 50)  # Edge from 0 to 2 with weight 50
        '''
        self.__test.append(('''(0, 2, 50)  # Edge from 0 to 2 with weight 50 ''',self.guard201,self.act201))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''(0, 2, 50)  # Edge from 0 to 2 with weight 50 '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            (0, 2, 50)  # Edge from 0 to 2 with weight 50
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard201(self):
        return True
    
    def act202(self):
        '''
        ]
        '''
        self.__test.append(('''] ''',self.guard202,self.act202))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''] '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            ]
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard202(self):
        return True
    
    def act203(self):
        '''
        graph_handler.add_edges(edges)
        '''
        self.__test.append(('''graph_handler.add_edges(edges) ''',self.guard203,self.act203))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''graph_handler.add_edges(edges) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            graph_handler.add_edges(edges)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard203(self):
        return True
    
    def act204(self):
        '''
        graph_handler.render_graph()
        '''
        self.__test.append(('''graph_handler.render_graph() ''',self.guard204,self.act204))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''graph_handler.render_graph() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            graph_handler.render_graph()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard204(self):
        return True
    
    def act205(self):
        '''
        graph_handler.visualize_graph()
        '''
        self.__test.append(('''graph_handler.visualize_graph() ''',self.guard205,self.act205))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''graph_handler.visualize_graph() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            graph_handler.visualize_graph()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard205(self):
        return True
    
    def act206(self):
        '''
        graph_handler.cycle_detection_summary()
        '''
        self.__test.append(('''graph_handler.cycle_detection_summary() ''',self.guard206,self.act206))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''graph_handler.cycle_detection_summary() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            graph_handler.cycle_detection_summary()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard206(self):
        return True
    
    def act207(self):
        '''
        cycle_analysis = GraphCycleAnalysis(graph_handler.graph)
        '''
        self.__test.append(('''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) ''',self.guard207,self.act207))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            cycle_analysis = GraphCycleAnalysis(graph_handler.graph)
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard207(self):
        return True
    
    def act208(self):
        '''
        cycle_analysis.analyze_cycles()
        '''
        self.__test.append(('''cycle_analysis.analyze_cycles() ''',self.guard208,self.act208))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''cycle_analysis.analyze_cycles() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            cycle_analysis.analyze_cycles()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard208(self):
        return True
    
    def act209(self):
        '''
        cycle_analysis.print_analysis()
        '''
        self.__test.append(('''cycle_analysis.print_analysis() ''',self.guard209,self.act209))
        self.__raised = None
        self.__refRaised = None
        if self.__verboseActions:
            __bV = {}
            print('ACTION:',self.prettyName('''cycle_analysis.print_analysis() '''))
        if self.__collectCov: self.__cov.start()
        try: test_before_each(self)
        except: pass
        try:
            cycle_analysis.print_analysis()
        except Exception as exc:
            raised = exc
            if self.__verboseActions: print('RAISED EXCEPTION:',type(raised),raised)
            raise
        finally:
            try: self.__raised = raised
            except: pass
            try: test_after_each(self)
            except: pass
            if self.__collectCov: self.__cov.stop(); self.__updateCov()
        if self.__verboseActions: print('='*50)
    def guard209(self):
        return True
    
    def __init__(self):
        try:
            test_before_all(self)
        except:
            pass
        self.__modules = []
        self.__importModules = []
        self.__features = []
        self.__replayBacktrack = False
        self.__cov = coverage.coverage(branch=True, source=self.moduleLocations(),    omit='sut.py'    )
        self.__cov._warn_no_data = False
        self.__collectCov = True
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
        self.__oldCovData = None
        self.__useCould = False
        self.__actionCould = True
        self.verboseActionCould = False
        self.__test = []
        self.__failure = None
        self.__warning = None
        self.__raised = None
        self.__refRaised = None
        self.__poolsNone = set([])
        self.__poolsUsed = set([])
        self.__disabledByNone = set([])
        self.__disabledByUsed = set([])
    # BEGIN INITIALIZATION CODE
    # END INITIALIZATION CODE
        self.__SUTName = """exp1.py"""
        self.__actions = []
        self.__names = {}
        self.__poolPrefix = "self.p_"
        self.__names["<<RESTART>>"] = ("<<RESTART>>", lambda x: True, lambda x: self.restart())
        self.__actionClass = {}
        self.__swarmConfig = None
        self.__actionClasses = []
        self.__essentialClasses = []
        self.__actionClasses.append('''from collections import defaultdict ''')
        self.__actionClasses.append('''class WeightedGraph: ''')
        self.__actionClasses.append('''    def __init__(self, vertices): ''')
        self.__actionClasses.append('''        self.vertices = vertices ''')
        self.__actionClasses.append('''        self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph ''')
        self.__actionClasses.append('''        self.edges = []  # List to store the edges (u, v, weight) ''')
        self.__actionClasses.append('''    def add_edge(self, u, v, weight): ''')
        self.__actionClasses.append('''        """Add a single edge to the graph.""" ''')
        self.__actionClasses.append('''        if (u, v, weight) not in self.edges: ''')
        self.__actionClasses.append('''            self.edges.append((u, v, weight)) ''')
        self.__actionClasses.append('''            self.adj_list[u].append((v, weight)) ''')
        self.__actionClasses.append('''    def add_multiple_edges(self, edges): ''')
        self.__actionClasses.append('''        """Add multiple edges at once.""" ''')
        self.__actionClasses.append('''        for u, v, weight in edges: ''')
        self.__actionClasses.append('''            self.add_edge(u, v, weight) ''')
        self.__actionClasses.append('''    def get_edges(self): ''')
        self.__actionClasses.append('''        """Return all edges in the graph.""" ''')
        self.__actionClasses.append('''        return self.edges ''')
        self.__actionClasses.append('''    def print_edges(self): ''')
        self.__actionClasses.append('''        """Print the edges of the graph.""" ''')
        self.__actionClasses.append('''        print("Edges in the graph:") ''')
        self.__actionClasses.append('''        for u, v, weight in self.edges: ''')
        self.__actionClasses.append('''            print(f"{u} -> {v} (Weight: {weight})") ''')
        self.__actionClasses.append('''    def print_adj_list(self): ''')
        self.__actionClasses.append('''        """Print the adjacency list of the graph.""" ''')
        self.__actionClasses.append('''        print("Adjacency List of the graph:") ''')
        self.__actionClasses.append('''        for u in self.adj_list: ''')
        self.__actionClasses.append('''            print(f"{u} -> {self.adj_list[u]}") ''')
        self.__actionClasses.append('''    def is_cyclic_directed(self): ''')
        self.__actionClasses.append('''        """Detect if there is a cycle in a directed graph using DFS.""" ''')
        self.__actionClasses.append('''        visited = [False] * self.vertices ''')
        self.__actionClasses.append('''        rec_stack = [False] * self.vertices ''')
        self.__actionClasses.append('''        def dfs(v): ''')
        self.__actionClasses.append('''            visited[v] = True ''')
        self.__actionClasses.append('''            rec_stack[v] = True ''')
        self.__actionClasses.append('''            for neighbor, _ in self.adj_list[v]: ''')
        self.__actionClasses.append('''                if not visited[neighbor] and dfs(neighbor): ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''                elif rec_stack[neighbor]: ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''            rec_stack[v] = False ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''        for node in range(self.vertices): ''')
        self.__actionClasses.append('''            if not visited[node]: ''')
        self.__actionClasses.append('''                if dfs(node): ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''    def is_cyclic_undirected(self): ''')
        self.__actionClasses.append('''        """Detect if there is a cycle in an undirected graph using DFS.""" ''')
        self.__actionClasses.append('''        visited = [False] * self.vertices ''')
        self.__actionClasses.append('''        def dfs(v, parent): ''')
        self.__actionClasses.append('''            visited[v] = True ''')
        self.__actionClasses.append('''            for neighbor, _ in self.adj_list[v]: ''')
        self.__actionClasses.append('''                if not visited[neighbor]: ''')
        self.__actionClasses.append('''                    if dfs(neighbor, v): ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''                elif parent != neighbor: ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''        for node in range(self.vertices): ''')
        self.__actionClasses.append('''            if not visited[node]: ''')
        self.__actionClasses.append('''                if dfs(node, -1): ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''    def is_negative_cycle(self): ''')
        self.__actionClasses.append('''        """Detect if there is a negative cycle using Bellman-Ford.""" ''')
        self.__actionClasses.append('''        dist = [float("inf")] * self.vertices ''')
        self.__actionClasses.append('''        dist[0] = 0  # Start from node 0 ''')
        self.__actionClasses.append('''        for _ in range(self.vertices - 1): ''')
        self.__actionClasses.append('''        for u, v, weight in self.edges: ''')
        self.__actionClasses.append('''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''')
        self.__actionClasses.append('''                    dist[v] = dist[u] + weight ''')
        self.__actionClasses.append('''        for u, v, weight in self.edges: ''')
        self.__actionClasses.append('''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''')
        self.__actionClasses.append('''                return True  # Negative cycle detected ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''    def reset_graph(self): ''')
        self.__actionClasses.append('''        """Reset the graph to its empty state.""" ''')
        self.__actionClasses.append('''        self.edges = []  # Clear all edges ''')
        self.__actionClasses.append('''        self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex ''')
        self.__actionClasses.append('''    def union(self, parent, u, v): ''')
        self.__actionClasses.append('''        """Union-find helper function.""" ''')
        self.__actionClasses.append('''        root_u = self.find_parent(parent, u) ''')
        self.__actionClasses.append('''        root_v = self.find_parent(parent, v) ''')
        self.__actionClasses.append('''        if root_u != root_v: ''')
        self.__actionClasses.append('''            parent[root_u] = root_v ''')
        self.__actionClasses.append('''    def find_parent(self, parent, v): ''')
        self.__actionClasses.append('''        """Find the root of the node using path compression.""" ''')
        self.__actionClasses.append('''        if parent[v] == -1: ''')
        self.__actionClasses.append('''            return v ''')
        self.__actionClasses.append('''        parent[v] = self.find_parent(parent, parent[v]) ''')
        self.__actionClasses.append('''        return parent[v] ''')
        self.__actionClasses.append('''    def is_cyclic_undirected_union_find(self): ''')
        self.__actionClasses.append('''        """Detect cycles in an undirected graph using Union-Find.""" ''')
        self.__actionClasses.append('''        parent = [-1] * self.vertices ''')
        self.__actionClasses.append('''        for u, v, _ in self.edges: ''')
        self.__actionClasses.append('''            x = self.find_parent(parent, u) ''')
        self.__actionClasses.append('''            y = self.find_parent(parent, v) ''')
        self.__actionClasses.append('''            if x == y: ''')
        self.__actionClasses.append('''                return True ''')
        self.__actionClasses.append('''            self.union(parent, x, y) ''')
        self.__actionClasses.append('''        return False ''')
        self.__actionClasses.append('''    def reset_graph_helper(self): ''')
        self.__actionClasses.append('''        """Reset the graph to an empty state for testing.""" ''')
        self.__actionClasses.append('''        self.edges = [] ''')
        self.__actionClasses.append('''        self.adj_list = defaultdict(list) ''')
        self.__actionClasses.append('''    def get_edges_helper(self): ''')
        self.__actionClasses.append('''        """Return all edges for testing.""" ''')
        self.__actionClasses.append('''        return self.edges ''')
        self.__actionClasses.append('''    def add_multiple_edges_helper(self, edges): ''')
        self.__actionClasses.append('''        """Add multiple edges for testing.""" ''')
        self.__actionClasses.append('''        for edge in edges: ''')
        self.__actionClasses.append('''            self.add_edge(*edge) ''')
        self.__actionClasses.append('''class CycleDetectionResults: ''')
        self.__actionClasses.append('''    def __init__(self): ''')
        self.__actionClasses.append('''        self.directed_cycle_detected = False ''')
        self.__actionClasses.append('''        self.undirected_cycle_detected = False ''')
        self.__actionClasses.append('''        self.negative_cycle_detected = False ''')
        self.__actionClasses.append('''class GraphRenderer: ''')
        self.__actionClasses.append('''    def __init__(self, graph): ''')
        self.__actionClasses.append('''        """Initialize the renderer for visualizing the graph.""" ''')
        self.__actionClasses.append('''        self.graph = graph ''')
        self.__actionClasses.append('''    def render_edges(self): ''')
        self.__actionClasses.append('''        """Render the edges of the graph.""" ''')
        self.__actionClasses.append('''        print("\nRendering edges of the graph:") ''')
        self.__actionClasses.append('''        for u, v, weight in self.graph.get_edges(): ''')
        self.__actionClasses.append('''            print(f"{u} -> {v} (Weight: {weight})") ''')
        self.__actionClasses.append('''    def render_adj_list(self): ''')
        self.__actionClasses.append('''        """Render the adjacency list of the graph.""" ''')
        self.__actionClasses.append('''        print("\nRendering adjacency list:") ''')
        self.__actionClasses.append('''        self.graph.print_adj_list() ''')
        self.__actionClasses.append('''    def render_summary(self): ''')
        self.__actionClasses.append('''        """Render a summary of the graph.""" ''')
        self.__actionClasses.append('''        print("\nGraph summary:") ''')
        self.__actionClasses.append('''        print(f"Total vertices: {self.graph.vertices}") ''')
        self.__actionClasses.append('''        print(f"Total edges: {len(self.graph.get_edges())}") ''')
        self.__actionClasses.append('''        print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") ''')
        self.__actionClasses.append('''        print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") ''')
        self.__actionClasses.append('''        print(f"Has negative cycle: {self.graph.is_negative_cycle()}") ''')
        self.__actionClasses.append('''import matplotlib.pyplot as plt ''')
        self.__actionClasses.append('''import networkx as nx ''')
        self.__actionClasses.append('''class WeightedGraphVisualization: ''')
        self.__actionClasses.append('''    def __init__(self, graph): ''')
        self.__actionClasses.append('''        """Initialize the visualization of weighted graph.""" ''')
        self.__actionClasses.append('''        self.graph = graph ''')
        self.__actionClasses.append('''    def visualize(self): ''')
        self.__actionClasses.append('''        """Visualize the graph with weighted edges using networkx and matplotlib.""" ''')
        self.__actionClasses.append('''        G = nx.DiGraph()  # Using DiGraph for directed graph visualization ''')
        self.__actionClasses.append('''        for u, v, weight in self.graph.get_edges(): ''')
        self.__actionClasses.append('''            G.add_edge(u, v, weight=weight) ''')
        self.__actionClasses.append('''        pos = nx.spring_layout(G)  # Layout for node positioning ''')
        self.__actionClasses.append('''        edge_labels = nx.get_edge_attributes(G, 'weight') ''')
        self.__actionClasses.append('''        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') ''')
        self.__actionClasses.append('''        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) ''')
        self.__actionClasses.append('''        plt.title("Graph Visualization with Weighted Edges") ''')
        self.__actionClasses.append('''        plt.show() ''')
        self.__actionClasses.append('''class WeightedGraphHandler: ''')
        self.__actionClasses.append('''    def __init__(self, vertices): ''')
        self.__actionClasses.append('''        """Initialize the graph handler.""" ''')
        self.__actionClasses.append('''        self.graph = WeightedGraph(vertices) ''')
        self.__actionClasses.append('''        self.renderer = GraphRenderer(self.graph) ''')
        self.__actionClasses.append('''        self.visualizer = WeightedGraphVisualization(self.graph) ''')
        self.__actionClasses.append('''    def add_edges(self, edges): ''')
        self.__actionClasses.append('''        """Add edges to the graph.""" ''')
        self.__actionClasses.append('''        for edge in edges: ''')
        self.__actionClasses.append('''            self.graph.add_edge(*edge) ''')
        self.__actionClasses.append('''    def render_graph(self): ''')
        self.__actionClasses.append('''        """Render the graph using the renderer.""" ''')
        self.__actionClasses.append('''        self.renderer.render_edges() ''')
        self.__actionClasses.append('''        self.renderer.render_adj_list() ''')
        self.__actionClasses.append('''    def visualize_graph(self): ''')
        self.__actionClasses.append('''        """Visualize the graph using the visualizer.""" ''')
        self.__actionClasses.append('''        self.visualizer.visualize() ''')
        self.__actionClasses.append('''    def cycle_detection_summary(self): ''')
        self.__actionClasses.append('''        """Print the cycle detection summary.""" ''')
        self.__actionClasses.append('''        print("\nCycle detection summary:") ''')
        self.__actionClasses.append('''        print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") ''')
        self.__actionClasses.append('''        print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") ''')
        self.__actionClasses.append('''        print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") ''')
        self.__actionClasses.append('''class GraphCycleAnalysis: ''')
        self.__actionClasses.append('''    def __init__(self, graph): ''')
        self.__actionClasses.append('''        """Initialize cycle analysis on the graph.""" ''')
        self.__actionClasses.append('''        self.graph = graph ''')
        self.__actionClasses.append('''        self.results = CycleDetectionResults() ''')
        self.__actionClasses.append('''    def analyze_cycles(self): ''')
        self.__actionClasses.append('''        """Analyze different types of cycles in the graph.""" ''')
        self.__actionClasses.append('''        self.results.directed_cycle_detected = self.graph.is_cyclic_directed() ''')
        self.__actionClasses.append('''        self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() ''')
        self.__actionClasses.append('''        self.results.negative_cycle_detected = self.graph.is_negative_cycle() ''')
        self.__actionClasses.append('''    def print_analysis(self): ''')
        self.__actionClasses.append('''        """Print the analysis results.""" ''')
        self.__actionClasses.append('''        print(f"Directed cycle detected: {self.results.directed_cycle_detected}") ''')
        self.__actionClasses.append('''        print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") ''')
        self.__actionClasses.append('''        print(f"Negative cycle detected: {self.results.negative_cycle_detected}") ''')
        self.__actionClasses.append('''if __name__ == "__main__": ''')
        self.__actionClasses.append('''    graph_handler = WeightedGraphHandler(4) ''')
        self.__actionClasses.append('''    edges = [ ''')
        self.__actionClasses.append('''        (0, 1, 10),  # Edge from 0 to 1 with weight 10 ''')
        self.__actionClasses.append('''        (1, 2, 20),  # Edge from 1 to 2 with weight 20 ''')
        self.__actionClasses.append('''        (2, 3, 30),  # Edge from 2 to 3 with weight 30 ''')
        self.__actionClasses.append('''        (3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0 -> 1 -> 2 -> 3 -> 0) ''')
        self.__actionClasses.append('''        (0, 2, 50)  # Edge from 0 to 2 with weight 50 ''')
        self.__actionClasses.append('''    ] ''')
        self.__actionClasses.append('''    graph_handler.add_edges(edges) ''')
        self.__actionClasses.append('''    graph_handler.render_graph() ''')
        self.__actionClasses.append('''    graph_handler.visualize_graph() ''')
        self.__actionClasses.append('''    graph_handler.cycle_detection_summary() ''')
        self.__actionClasses.append('''    cycle_analysis = GraphCycleAnalysis(graph_handler.graph) ''')
        self.__actionClasses.append('''    cycle_analysis.analyze_cycles() ''')
        self.__actionClasses.append('''    cycle_analysis.print_analysis() ''')
        self.__dependencies = {}
        self.__dependencies['''from collections import defaultdict '''] = []
        self.__dependencies['''class WeightedGraph: '''] = []
        self.__dependencies['''    def __init__(self, vertices): '''] = []
        self.__dependencies['''        self.vertices = vertices '''] = []
        self.__dependencies['''        self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''] = []
        self.__dependencies['''        self.edges = []  # List to store the edges (u, v, weight) '''] = []
        self.__dependencies['''    def add_edge(self, u, v, weight): '''] = []
        self.__dependencies['''        """Add a single edge to the graph.""" '''] = []
        self.__dependencies['''        if (u, v, weight) not in self.edges: '''] = []
        self.__dependencies['''            self.edges.append((u, v, weight)) '''] = []
        self.__dependencies['''            self.adj_list[u].append((v, weight)) '''] = []
        self.__dependencies['''    def add_multiple_edges(self, edges): '''] = []
        self.__dependencies['''        """Add multiple edges at once.""" '''] = []
        self.__dependencies['''        for u, v, weight in edges: '''] = []
        self.__dependencies['''            self.add_edge(u, v, weight) '''] = []
        self.__dependencies['''    def get_edges(self): '''] = []
        self.__dependencies['''        """Return all edges in the graph.""" '''] = []
        self.__dependencies['''        return self.edges '''] = []
        self.__dependencies['''    def print_edges(self): '''] = []
        self.__dependencies['''        """Print the edges of the graph.""" '''] = []
        self.__dependencies['''        print("Edges in the graph:") '''] = []
        self.__dependencies['''        for u, v, weight in self.edges: '''] = []
        self.__dependencies['''            print(f"{u} -> {v} (Weight: {weight})") '''] = []
        self.__dependencies['''    def print_adj_list(self): '''] = []
        self.__dependencies['''        """Print the adjacency list of the graph.""" '''] = []
        self.__dependencies['''        print("Adjacency List of the graph:") '''] = []
        self.__dependencies['''        for u in self.adj_list: '''] = []
        self.__dependencies['''            print(f"{u} -> {self.adj_list[u]}") '''] = []
        self.__dependencies['''    def is_cyclic_directed(self): '''] = []
        self.__dependencies['''        """Detect if there is a cycle in a directed graph using DFS.""" '''] = []
        self.__dependencies['''        visited = [False] * self.vertices '''] = []
        self.__dependencies['''        rec_stack = [False] * self.vertices '''] = []
        self.__dependencies['''        def dfs(v): '''] = []
        self.__dependencies['''            visited[v] = True '''] = []
        self.__dependencies['''            rec_stack[v] = True '''] = []
        self.__dependencies['''            for neighbor, _ in self.adj_list[v]: '''] = []
        self.__dependencies['''                if not visited[neighbor] and dfs(neighbor): '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''                elif rec_stack[neighbor]: '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''            rec_stack[v] = False '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''        for node in range(self.vertices): '''] = []
        self.__dependencies['''            if not visited[node]: '''] = []
        self.__dependencies['''                if dfs(node): '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''    def is_cyclic_undirected(self): '''] = []
        self.__dependencies['''        """Detect if there is a cycle in an undirected graph using DFS.""" '''] = []
        self.__dependencies['''        visited = [False] * self.vertices '''] = []
        self.__dependencies['''        def dfs(v, parent): '''] = []
        self.__dependencies['''            visited[v] = True '''] = []
        self.__dependencies['''            for neighbor, _ in self.adj_list[v]: '''] = []
        self.__dependencies['''                if not visited[neighbor]: '''] = []
        self.__dependencies['''                    if dfs(neighbor, v): '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''                elif parent != neighbor: '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''        for node in range(self.vertices): '''] = []
        self.__dependencies['''            if not visited[node]: '''] = []
        self.__dependencies['''                if dfs(node, -1): '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''    def is_negative_cycle(self): '''] = []
        self.__dependencies['''        """Detect if there is a negative cycle using Bellman-Ford.""" '''] = []
        self.__dependencies['''        dist = [float("inf")] * self.vertices '''] = []
        self.__dependencies['''        dist[0] = 0  # Start from node 0 '''] = []
        self.__dependencies['''        for _ in range(self.vertices - 1): '''] = []
        self.__dependencies['''        for u, v, weight in self.edges: '''] = []
        self.__dependencies['''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = []
        self.__dependencies['''                    dist[v] = dist[u] + weight '''] = []
        self.__dependencies['''        for u, v, weight in self.edges: '''] = []
        self.__dependencies['''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = []
        self.__dependencies['''                return True  # Negative cycle detected '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''    def reset_graph(self): '''] = []
        self.__dependencies['''        """Reset the graph to its empty state.""" '''] = []
        self.__dependencies['''        self.edges = []  # Clear all edges '''] = []
        self.__dependencies['''        self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''] = []
        self.__dependencies['''    def union(self, parent, u, v): '''] = []
        self.__dependencies['''        """Union-find helper function.""" '''] = []
        self.__dependencies['''        root_u = self.find_parent(parent, u) '''] = []
        self.__dependencies['''        root_v = self.find_parent(parent, v) '''] = []
        self.__dependencies['''        if root_u != root_v: '''] = []
        self.__dependencies['''            parent[root_u] = root_v '''] = []
        self.__dependencies['''    def find_parent(self, parent, v): '''] = []
        self.__dependencies['''        """Find the root of the node using path compression.""" '''] = []
        self.__dependencies['''        if parent[v] == -1: '''] = []
        self.__dependencies['''            return v '''] = []
        self.__dependencies['''        parent[v] = self.find_parent(parent, parent[v]) '''] = []
        self.__dependencies['''        return parent[v] '''] = []
        self.__dependencies['''    def is_cyclic_undirected_union_find(self): '''] = []
        self.__dependencies['''        """Detect cycles in an undirected graph using Union-Find.""" '''] = []
        self.__dependencies['''        parent = [-1] * self.vertices '''] = []
        self.__dependencies['''        for u, v, _ in self.edges: '''] = []
        self.__dependencies['''            x = self.find_parent(parent, u) '''] = []
        self.__dependencies['''            y = self.find_parent(parent, v) '''] = []
        self.__dependencies['''            if x == y: '''] = []
        self.__dependencies['''                return True '''] = []
        self.__dependencies['''            self.union(parent, x, y) '''] = []
        self.__dependencies['''        return False '''] = []
        self.__dependencies['''    def reset_graph_helper(self): '''] = []
        self.__dependencies['''        """Reset the graph to an empty state for testing.""" '''] = []
        self.__dependencies['''        self.edges = [] '''] = []
        self.__dependencies['''        self.adj_list = defaultdict(list) '''] = []
        self.__dependencies['''    def get_edges_helper(self): '''] = []
        self.__dependencies['''        """Return all edges for testing.""" '''] = []
        self.__dependencies['''        return self.edges '''] = []
        self.__dependencies['''    def add_multiple_edges_helper(self, edges): '''] = []
        self.__dependencies['''        """Add multiple edges for testing.""" '''] = []
        self.__dependencies['''        for edge in edges: '''] = []
        self.__dependencies['''            self.add_edge(*edge) '''] = []
        self.__dependencies['''class CycleDetectionResults: '''] = []
        self.__dependencies['''    def __init__(self): '''] = []
        self.__dependencies['''        self.directed_cycle_detected = False '''] = []
        self.__dependencies['''        self.undirected_cycle_detected = False '''] = []
        self.__dependencies['''        self.negative_cycle_detected = False '''] = []
        self.__dependencies['''class GraphRenderer: '''] = []
        self.__dependencies['''    def __init__(self, graph): '''] = []
        self.__dependencies['''        """Initialize the renderer for visualizing the graph.""" '''] = []
        self.__dependencies['''        self.graph = graph '''] = []
        self.__dependencies['''    def render_edges(self): '''] = []
        self.__dependencies['''        """Render the edges of the graph.""" '''] = []
        self.__dependencies['''        print("\nRendering edges of the graph:") '''] = []
        self.__dependencies['''        for u, v, weight in self.graph.get_edges(): '''] = []
        self.__dependencies['''            print(f"{u} -> {v} (Weight: {weight})") '''] = []
        self.__dependencies['''    def render_adj_list(self): '''] = []
        self.__dependencies['''        """Render the adjacency list of the graph.""" '''] = []
        self.__dependencies['''        print("\nRendering adjacency list:") '''] = []
        self.__dependencies['''        self.graph.print_adj_list() '''] = []
        self.__dependencies['''    def render_summary(self): '''] = []
        self.__dependencies['''        """Render a summary of the graph.""" '''] = []
        self.__dependencies['''        print("\nGraph summary:") '''] = []
        self.__dependencies['''        print(f"Total vertices: {self.graph.vertices}") '''] = []
        self.__dependencies['''        print(f"Total edges: {len(self.graph.get_edges())}") '''] = []
        self.__dependencies['''        print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''] = []
        self.__dependencies['''        print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''] = []
        self.__dependencies['''        print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''] = []
        self.__dependencies['''import matplotlib.pyplot as plt '''] = []
        self.__dependencies['''import networkx as nx '''] = []
        self.__dependencies['''class WeightedGraphVisualization: '''] = []
        self.__dependencies['''    def __init__(self, graph): '''] = []
        self.__dependencies['''        """Initialize the visualization of weighted graph.""" '''] = []
        self.__dependencies['''        self.graph = graph '''] = []
        self.__dependencies['''    def visualize(self): '''] = []
        self.__dependencies['''        """Visualize the graph with weighted edges using networkx and matplotlib.""" '''] = []
        self.__dependencies['''        G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''] = []
        self.__dependencies['''        for u, v, weight in self.graph.get_edges(): '''] = []
        self.__dependencies['''            G.add_edge(u, v, weight=weight) '''] = []
        self.__dependencies['''        pos = nx.spring_layout(G)  # Layout for node positioning '''] = []
        self.__dependencies['''        edge_labels = nx.get_edge_attributes(G, 'weight') '''] = []
        self.__dependencies['''        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''] = []
        self.__dependencies['''        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''] = []
        self.__dependencies['''        plt.title("Graph Visualization with Weighted Edges") '''] = []
        self.__dependencies['''        plt.show() '''] = []
        self.__dependencies['''class WeightedGraphHandler: '''] = []
        self.__dependencies['''    def __init__(self, vertices): '''] = []
        self.__dependencies['''        """Initialize the graph handler.""" '''] = []
        self.__dependencies['''        self.graph = WeightedGraph(vertices) '''] = []
        self.__dependencies['''        self.renderer = GraphRenderer(self.graph) '''] = []
        self.__dependencies['''        self.visualizer = WeightedGraphVisualization(self.graph) '''] = []
        self.__dependencies['''    def add_edges(self, edges): '''] = []
        self.__dependencies['''        """Add edges to the graph.""" '''] = []
        self.__dependencies['''        for edge in edges: '''] = []
        self.__dependencies['''            self.graph.add_edge(*edge) '''] = []
        self.__dependencies['''    def render_graph(self): '''] = []
        self.__dependencies['''        """Render the graph using the renderer.""" '''] = []
        self.__dependencies['''        self.renderer.render_edges() '''] = []
        self.__dependencies['''        self.renderer.render_adj_list() '''] = []
        self.__dependencies['''    def visualize_graph(self): '''] = []
        self.__dependencies['''        """Visualize the graph using the visualizer.""" '''] = []
        self.__dependencies['''        self.visualizer.visualize() '''] = []
        self.__dependencies['''    def cycle_detection_summary(self): '''] = []
        self.__dependencies['''        """Print the cycle detection summary.""" '''] = []
        self.__dependencies['''        print("\nCycle detection summary:") '''] = []
        self.__dependencies['''        print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''] = []
        self.__dependencies['''        print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''] = []
        self.__dependencies['''        print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''] = []
        self.__dependencies['''class GraphCycleAnalysis: '''] = []
        self.__dependencies['''    def __init__(self, graph): '''] = []
        self.__dependencies['''        """Initialize cycle analysis on the graph.""" '''] = []
        self.__dependencies['''        self.graph = graph '''] = []
        self.__dependencies['''        self.results = CycleDetectionResults() '''] = []
        self.__dependencies['''    def analyze_cycles(self): '''] = []
        self.__dependencies['''        """Analyze different types of cycles in the graph.""" '''] = []
        self.__dependencies['''        self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''] = []
        self.__dependencies['''        self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''] = []
        self.__dependencies['''        self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''] = []
        self.__dependencies['''    def print_analysis(self): '''] = []
        self.__dependencies['''        """Print the analysis results.""" '''] = []
        self.__dependencies['''        print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''] = []
        self.__dependencies['''        print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''] = []
        self.__dependencies['''        print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''] = []
        self.__dependencies['''if __name__ == "__main__": '''] = []
        self.__dependencies['''    graph_handler = WeightedGraphHandler(4) '''] = []
        self.__dependencies['''    edges = [ '''] = []
        self.__dependencies['''        (0, 1, 10),  # Edge from 0 to 1 with weight 10 '''] = []
        self.__dependencies['''        (1, 2, 20),  # Edge from 1 to 2 with weight 20 '''] = []
        self.__dependencies['''        (2, 3, 30),  # Edge from 2 to 3 with weight 30 '''] = []
        self.__dependencies['''        (3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0 -> 1 -> 2 -> 3 -> 0) '''] = []
        self.__dependencies['''        (0, 2, 50)  # Edge from 0 to 2 with weight 50 '''] = []
        self.__dependencies['''    ] '''] = []
        self.__dependencies['''    graph_handler.add_edges(edges) '''] = []
        self.__dependencies['''    graph_handler.render_graph() '''] = []
        self.__dependencies['''    graph_handler.visualize_graph() '''] = []
        self.__dependencies['''    graph_handler.cycle_detection_summary() '''] = []
        self.__dependencies['''    cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''] = []
        self.__dependencies['''    cycle_analysis.analyze_cycles() '''] = []
        self.__dependencies['''    cycle_analysis.print_analysis() '''] = []
        self.__orderings = {}
        self.__okExcepts = {}
        self.__preCode = {}
        self.__refCode = {}
        self.__propCode = {}
        self.__orderings["<<RESTART>>"] = -1
        self.__log = None
        self.__enumerateEnabled = False
        self.__verboseActions = False
        self.__verbosePrintOpaque = True
        self.__logAction = self.logPrint
        self.__relaxUsedRestriction = False
        self.__doReload = True
        self.__assumptionViolated = None
        self.__noReassigns = False
        self.__safeSafelyMode = False
        self.__simplifyCache = {}
        self.__fastPoolStates = True
        self.__pools = []
        self.__poolUsers = {}
        self.__poolInitializers = {}
        self.__psize = {}
        self.__consts = []
        self.__opaque = []
        self.__abstraction = {}
        if self.__useCould: self.computeInitialEnabled()
        
        self.__actions.append(('''from collections import defaultdict ''',self.guard0,self.act0))
        self.__names['''from collections import defaultdict '''] = ('''from collections import defaultdict ''',self.guard0,self.act0)
        self.__actionClass['''from collections import defaultdict '''] = '''from collections import defaultdict '''
        self.__orderings['''from collections import defaultdict '''] = 1
        self.__okExcepts['''from collections import defaultdict '''] = ''''''
        
        self.__actions.append(('''class WeightedGraph: ''',self.guard1,self.act1))
        self.__names['''class WeightedGraph: '''] = ('''class WeightedGraph: ''',self.guard1,self.act1)
        self.__actionClass['''class WeightedGraph: '''] = '''class WeightedGraph: '''
        self.__orderings['''class WeightedGraph: '''] = 2
        self.__okExcepts['''class WeightedGraph: '''] = ''''''
        
        self.__actions.append(('''def __init__(self, vertices): ''',self.guard2,self.act2))
        self.__names['''def __init__(self, vertices): '''] = ('''def __init__(self, vertices): ''',self.guard2,self.act2)
        self.__actionClass['''def __init__(self, vertices): '''] = '''    def __init__(self, vertices): '''
        self.__orderings['''def __init__(self, vertices): '''] = 3
        self.__okExcepts['''def __init__(self, vertices): '''] = ''''''
        
        self.__actions.append(('''self.vertices = vertices ''',self.guard3,self.act3))
        self.__names['''self.vertices = vertices '''] = ('''self.vertices = vertices ''',self.guard3,self.act3)
        self.__actionClass['''self.vertices = vertices '''] = '''        self.vertices = vertices '''
        self.__orderings['''self.vertices = vertices '''] = 4
        self.__okExcepts['''self.vertices = vertices '''] = ''''''
        
        self.__actions.append(('''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph ''',self.guard4,self.act4))
        self.__names['''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''] = ('''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph ''',self.guard4,self.act4)
        self.__actionClass['''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''] = '''        self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''
        self.__orderings['''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''] = 5
        self.__okExcepts['''self.adj_list = {i: [] for i in range(vertices)}  # Adjacency list for the graph '''] = ''''''
        
        self.__actions.append(('''self.edges = []  # List to store the edges (u, v, weight) ''',self.guard5,self.act5))
        self.__names['''self.edges = []  # List to store the edges (u, v, weight) '''] = ('''self.edges = []  # List to store the edges (u, v, weight) ''',self.guard5,self.act5)
        self.__actionClass['''self.edges = []  # List to store the edges (u, v, weight) '''] = '''        self.edges = []  # List to store the edges (u, v, weight) '''
        self.__orderings['''self.edges = []  # List to store the edges (u, v, weight) '''] = 6
        self.__okExcepts['''self.edges = []  # List to store the edges (u, v, weight) '''] = ''''''
        
        self.__actions.append(('''def add_edge(self, u, v, weight): ''',self.guard6,self.act6))
        self.__names['''def add_edge(self, u, v, weight): '''] = ('''def add_edge(self, u, v, weight): ''',self.guard6,self.act6)
        self.__actionClass['''def add_edge(self, u, v, weight): '''] = '''    def add_edge(self, u, v, weight): '''
        self.__orderings['''def add_edge(self, u, v, weight): '''] = 7
        self.__okExcepts['''def add_edge(self, u, v, weight): '''] = ''''''
        
        self.__actions.append(('''"""Add a single edge to the graph.""" ''',self.guard7,self.act7))
        self.__names['''"""Add a single edge to the graph.""" '''] = ('''"""Add a single edge to the graph.""" ''',self.guard7,self.act7)
        self.__actionClass['''"""Add a single edge to the graph.""" '''] = '''        """Add a single edge to the graph.""" '''
        self.__orderings['''"""Add a single edge to the graph.""" '''] = 8
        self.__okExcepts['''"""Add a single edge to the graph.""" '''] = ''''''
        
        self.__actions.append(('''if (u, v, weight) not in self.edges: ''',self.guard8,self.act8))
        self.__names['''if (u, v, weight) not in self.edges: '''] = ('''if (u, v, weight) not in self.edges: ''',self.guard8,self.act8)
        self.__actionClass['''if (u, v, weight) not in self.edges: '''] = '''        if (u, v, weight) not in self.edges: '''
        self.__orderings['''if (u, v, weight) not in self.edges: '''] = 9
        self.__okExcepts['''if (u, v, weight) not in self.edges: '''] = ''''''
        
        self.__actions.append(('''self.edges.append((u, v, weight)) ''',self.guard9,self.act9))
        self.__names['''self.edges.append((u, v, weight)) '''] = ('''self.edges.append((u, v, weight)) ''',self.guard9,self.act9)
        self.__actionClass['''self.edges.append((u, v, weight)) '''] = '''            self.edges.append((u, v, weight)) '''
        self.__orderings['''self.edges.append((u, v, weight)) '''] = 10
        self.__okExcepts['''self.edges.append((u, v, weight)) '''] = ''''''
        
        self.__actions.append(('''self.adj_list[u].append((v, weight)) ''',self.guard10,self.act10))
        self.__names['''self.adj_list[u].append((v, weight)) '''] = ('''self.adj_list[u].append((v, weight)) ''',self.guard10,self.act10)
        self.__actionClass['''self.adj_list[u].append((v, weight)) '''] = '''            self.adj_list[u].append((v, weight)) '''
        self.__orderings['''self.adj_list[u].append((v, weight)) '''] = 11
        self.__okExcepts['''self.adj_list[u].append((v, weight)) '''] = ''''''
        
        self.__actions.append(('''def add_multiple_edges(self, edges): ''',self.guard11,self.act11))
        self.__names['''def add_multiple_edges(self, edges): '''] = ('''def add_multiple_edges(self, edges): ''',self.guard11,self.act11)
        self.__actionClass['''def add_multiple_edges(self, edges): '''] = '''    def add_multiple_edges(self, edges): '''
        self.__orderings['''def add_multiple_edges(self, edges): '''] = 12
        self.__okExcepts['''def add_multiple_edges(self, edges): '''] = ''''''
        
        self.__actions.append(('''"""Add multiple edges at once.""" ''',self.guard12,self.act12))
        self.__names['''"""Add multiple edges at once.""" '''] = ('''"""Add multiple edges at once.""" ''',self.guard12,self.act12)
        self.__actionClass['''"""Add multiple edges at once.""" '''] = '''        """Add multiple edges at once.""" '''
        self.__orderings['''"""Add multiple edges at once.""" '''] = 13
        self.__okExcepts['''"""Add multiple edges at once.""" '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in edges: ''',self.guard13,self.act13))
        self.__names['''for u, v, weight in edges: '''] = ('''for u, v, weight in edges: ''',self.guard13,self.act13)
        self.__actionClass['''for u, v, weight in edges: '''] = '''        for u, v, weight in edges: '''
        self.__orderings['''for u, v, weight in edges: '''] = 14
        self.__okExcepts['''for u, v, weight in edges: '''] = ''''''
        
        self.__actions.append(('''self.add_edge(u, v, weight) ''',self.guard14,self.act14))
        self.__names['''self.add_edge(u, v, weight) '''] = ('''self.add_edge(u, v, weight) ''',self.guard14,self.act14)
        self.__actionClass['''self.add_edge(u, v, weight) '''] = '''            self.add_edge(u, v, weight) '''
        self.__orderings['''self.add_edge(u, v, weight) '''] = 15
        self.__okExcepts['''self.add_edge(u, v, weight) '''] = ''''''
        
        self.__actions.append(('''def get_edges(self): ''',self.guard15,self.act15))
        self.__names['''def get_edges(self): '''] = ('''def get_edges(self): ''',self.guard15,self.act15)
        self.__actionClass['''def get_edges(self): '''] = '''    def get_edges(self): '''
        self.__orderings['''def get_edges(self): '''] = 16
        self.__okExcepts['''def get_edges(self): '''] = ''''''
        
        self.__actions.append(('''"""Return all edges in the graph.""" ''',self.guard16,self.act16))
        self.__names['''"""Return all edges in the graph.""" '''] = ('''"""Return all edges in the graph.""" ''',self.guard16,self.act16)
        self.__actionClass['''"""Return all edges in the graph.""" '''] = '''        """Return all edges in the graph.""" '''
        self.__orderings['''"""Return all edges in the graph.""" '''] = 17
        self.__okExcepts['''"""Return all edges in the graph.""" '''] = ''''''
        
        self.__actions.append(('''return self.edges ''',self.guard17,self.act17))
        self.__names['''return self.edges '''] = ('''return self.edges ''',self.guard17,self.act17)
        self.__actionClass['''return self.edges '''] = '''        return self.edges '''
        self.__orderings['''return self.edges '''] = 18
        self.__okExcepts['''return self.edges '''] = ''''''
        
        self.__actions.append(('''def print_edges(self): ''',self.guard18,self.act18))
        self.__names['''def print_edges(self): '''] = ('''def print_edges(self): ''',self.guard18,self.act18)
        self.__actionClass['''def print_edges(self): '''] = '''    def print_edges(self): '''
        self.__orderings['''def print_edges(self): '''] = 19
        self.__okExcepts['''def print_edges(self): '''] = ''''''
        
        self.__actions.append(('''"""Print the edges of the graph.""" ''',self.guard19,self.act19))
        self.__names['''"""Print the edges of the graph.""" '''] = ('''"""Print the edges of the graph.""" ''',self.guard19,self.act19)
        self.__actionClass['''"""Print the edges of the graph.""" '''] = '''        """Print the edges of the graph.""" '''
        self.__orderings['''"""Print the edges of the graph.""" '''] = 20
        self.__okExcepts['''"""Print the edges of the graph.""" '''] = ''''''
        
        self.__actions.append(('''print("Edges in the graph:") ''',self.guard20,self.act20))
        self.__names['''print("Edges in the graph:") '''] = ('''print("Edges in the graph:") ''',self.guard20,self.act20)
        self.__actionClass['''print("Edges in the graph:") '''] = '''        print("Edges in the graph:") '''
        self.__orderings['''print("Edges in the graph:") '''] = 21
        self.__okExcepts['''print("Edges in the graph:") '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in self.edges: ''',self.guard21,self.act21))
        self.__names['''for u, v, weight in self.edges: '''] = ('''for u, v, weight in self.edges: ''',self.guard21,self.act21)
        self.__actionClass['''for u, v, weight in self.edges: '''] = '''        for u, v, weight in self.edges: '''
        self.__orderings['''for u, v, weight in self.edges: '''] = 22
        self.__okExcepts['''for u, v, weight in self.edges: '''] = ''''''
        
        self.__actions.append(('''{v} (Weight: {weight})") ''',self.guard22,self.act22))
        self.__names['''{v} (Weight: {weight})") '''] = ('''{v} (Weight: {weight})") ''',self.guard22,self.act22)
        self.__actionClass['''{v} (Weight: {weight})") '''] = '''            print(f"{u} -> {v} (Weight: {weight})") '''
        self.__orderings['''{v} (Weight: {weight})") '''] = 23
        self.__okExcepts['''{v} (Weight: {weight})") '''] = ''''''
        
        self.__actions.append(('''def print_adj_list(self): ''',self.guard23,self.act23))
        self.__names['''def print_adj_list(self): '''] = ('''def print_adj_list(self): ''',self.guard23,self.act23)
        self.__actionClass['''def print_adj_list(self): '''] = '''    def print_adj_list(self): '''
        self.__orderings['''def print_adj_list(self): '''] = 24
        self.__okExcepts['''def print_adj_list(self): '''] = ''''''
        
        self.__actions.append(('''"""Print the adjacency list of the graph.""" ''',self.guard24,self.act24))
        self.__names['''"""Print the adjacency list of the graph.""" '''] = ('''"""Print the adjacency list of the graph.""" ''',self.guard24,self.act24)
        self.__actionClass['''"""Print the adjacency list of the graph.""" '''] = '''        """Print the adjacency list of the graph.""" '''
        self.__orderings['''"""Print the adjacency list of the graph.""" '''] = 25
        self.__okExcepts['''"""Print the adjacency list of the graph.""" '''] = ''''''
        
        self.__actions.append(('''print("Adjacency List of the graph:") ''',self.guard25,self.act25))
        self.__names['''print("Adjacency List of the graph:") '''] = ('''print("Adjacency List of the graph:") ''',self.guard25,self.act25)
        self.__actionClass['''print("Adjacency List of the graph:") '''] = '''        print("Adjacency List of the graph:") '''
        self.__orderings['''print("Adjacency List of the graph:") '''] = 26
        self.__okExcepts['''print("Adjacency List of the graph:") '''] = ''''''
        
        self.__actions.append(('''for u in self.adj_list: ''',self.guard26,self.act26))
        self.__names['''for u in self.adj_list: '''] = ('''for u in self.adj_list: ''',self.guard26,self.act26)
        self.__actionClass['''for u in self.adj_list: '''] = '''        for u in self.adj_list: '''
        self.__orderings['''for u in self.adj_list: '''] = 27
        self.__okExcepts['''for u in self.adj_list: '''] = ''''''
        
        self.__actions.append(('''{self.adj_list[u]}") ''',self.guard27,self.act27))
        self.__names['''{self.adj_list[u]}") '''] = ('''{self.adj_list[u]}") ''',self.guard27,self.act27)
        self.__actionClass['''{self.adj_list[u]}") '''] = '''            print(f"{u} -> {self.adj_list[u]}") '''
        self.__orderings['''{self.adj_list[u]}") '''] = 28
        self.__okExcepts['''{self.adj_list[u]}") '''] = ''''''
        
        self.__actions.append(('''def is_cyclic_directed(self): ''',self.guard28,self.act28))
        self.__names['''def is_cyclic_directed(self): '''] = ('''def is_cyclic_directed(self): ''',self.guard28,self.act28)
        self.__actionClass['''def is_cyclic_directed(self): '''] = '''    def is_cyclic_directed(self): '''
        self.__orderings['''def is_cyclic_directed(self): '''] = 29
        self.__okExcepts['''def is_cyclic_directed(self): '''] = ''''''
        
        self.__actions.append(('''"""Detect if there is a cycle in a directed graph using DFS.""" ''',self.guard29,self.act29))
        self.__names['''"""Detect if there is a cycle in a directed graph using DFS.""" '''] = ('''"""Detect if there is a cycle in a directed graph using DFS.""" ''',self.guard29,self.act29)
        self.__actionClass['''"""Detect if there is a cycle in a directed graph using DFS.""" '''] = '''        """Detect if there is a cycle in a directed graph using DFS.""" '''
        self.__orderings['''"""Detect if there is a cycle in a directed graph using DFS.""" '''] = 30
        self.__okExcepts['''"""Detect if there is a cycle in a directed graph using DFS.""" '''] = ''''''
        
        self.__actions.append(('''visited = [False] * self.vertices ''',self.guard30,self.act30))
        self.__names['''visited = [False] * self.vertices '''] = ('''visited = [False] * self.vertices ''',self.guard30,self.act30)
        self.__actionClass['''visited = [False] * self.vertices '''] = '''        visited = [False] * self.vertices '''
        self.__orderings['''visited = [False] * self.vertices '''] = 31
        self.__okExcepts['''visited = [False] * self.vertices '''] = ''''''
        
        self.__actions.append(('''rec_stack = [False] * self.vertices ''',self.guard31,self.act31))
        self.__names['''rec_stack = [False] * self.vertices '''] = ('''rec_stack = [False] * self.vertices ''',self.guard31,self.act31)
        self.__actionClass['''rec_stack = [False] * self.vertices '''] = '''        rec_stack = [False] * self.vertices '''
        self.__orderings['''rec_stack = [False] * self.vertices '''] = 32
        self.__okExcepts['''rec_stack = [False] * self.vertices '''] = ''''''
        
        self.__actions.append(('''def dfs(v): ''',self.guard32,self.act32))
        self.__names['''def dfs(v): '''] = ('''def dfs(v): ''',self.guard32,self.act32)
        self.__actionClass['''def dfs(v): '''] = '''        def dfs(v): '''
        self.__orderings['''def dfs(v): '''] = 33
        self.__okExcepts['''def dfs(v): '''] = ''''''
        
        self.__actions.append(('''visited[v] = True ''',self.guard33,self.act33))
        self.__names['''visited[v] = True '''] = ('''visited[v] = True ''',self.guard33,self.act33)
        self.__actionClass['''visited[v] = True '''] = '''            visited[v] = True '''
        self.__orderings['''visited[v] = True '''] = 34
        self.__okExcepts['''visited[v] = True '''] = ''''''
        
        self.__actions.append(('''rec_stack[v] = True ''',self.guard34,self.act34))
        self.__names['''rec_stack[v] = True '''] = ('''rec_stack[v] = True ''',self.guard34,self.act34)
        self.__actionClass['''rec_stack[v] = True '''] = '''            rec_stack[v] = True '''
        self.__orderings['''rec_stack[v] = True '''] = 35
        self.__okExcepts['''rec_stack[v] = True '''] = ''''''
        
        self.__actions.append(('''for neighbor, _ in self.adj_list[v]: ''',self.guard35,self.act35))
        self.__names['''for neighbor, _ in self.adj_list[v]: '''] = ('''for neighbor, _ in self.adj_list[v]: ''',self.guard35,self.act35)
        self.__actionClass['''for neighbor, _ in self.adj_list[v]: '''] = '''            for neighbor, _ in self.adj_list[v]: '''
        self.__orderings['''for neighbor, _ in self.adj_list[v]: '''] = 36
        self.__okExcepts['''for neighbor, _ in self.adj_list[v]: '''] = ''''''
        
        self.__actions.append(('''if not visited[neighbor] and dfs(neighbor): ''',self.guard36,self.act36))
        self.__names['''if not visited[neighbor] and dfs(neighbor): '''] = ('''if not visited[neighbor] and dfs(neighbor): ''',self.guard36,self.act36)
        self.__actionClass['''if not visited[neighbor] and dfs(neighbor): '''] = '''                if not visited[neighbor] and dfs(neighbor): '''
        self.__orderings['''if not visited[neighbor] and dfs(neighbor): '''] = 37
        self.__okExcepts['''if not visited[neighbor] and dfs(neighbor): '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard37,self.act37))
        self.__names['''return True '''] = ('''return True ''',self.guard37,self.act37)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 38
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''elif rec_stack[neighbor]: ''',self.guard38,self.act38))
        self.__names['''elif rec_stack[neighbor]: '''] = ('''elif rec_stack[neighbor]: ''',self.guard38,self.act38)
        self.__actionClass['''elif rec_stack[neighbor]: '''] = '''                elif rec_stack[neighbor]: '''
        self.__orderings['''elif rec_stack[neighbor]: '''] = 39
        self.__okExcepts['''elif rec_stack[neighbor]: '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard39,self.act39))
        self.__names['''return True '''] = ('''return True ''',self.guard39,self.act39)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 40
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''rec_stack[v] = False ''',self.guard40,self.act40))
        self.__names['''rec_stack[v] = False '''] = ('''rec_stack[v] = False ''',self.guard40,self.act40)
        self.__actionClass['''rec_stack[v] = False '''] = '''            rec_stack[v] = False '''
        self.__orderings['''rec_stack[v] = False '''] = 41
        self.__okExcepts['''rec_stack[v] = False '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard41,self.act41))
        self.__names['''return False '''] = ('''return False ''',self.guard41,self.act41)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 42
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''for node in range(self.vertices): ''',self.guard42,self.act42))
        self.__names['''for node in range(self.vertices): '''] = ('''for node in range(self.vertices): ''',self.guard42,self.act42)
        self.__actionClass['''for node in range(self.vertices): '''] = '''        for node in range(self.vertices): '''
        self.__orderings['''for node in range(self.vertices): '''] = 43
        self.__okExcepts['''for node in range(self.vertices): '''] = ''''''
        
        self.__actions.append(('''if not visited[node]: ''',self.guard43,self.act43))
        self.__names['''if not visited[node]: '''] = ('''if not visited[node]: ''',self.guard43,self.act43)
        self.__actionClass['''if not visited[node]: '''] = '''            if not visited[node]: '''
        self.__orderings['''if not visited[node]: '''] = 44
        self.__okExcepts['''if not visited[node]: '''] = ''''''
        
        self.__actions.append(('''if dfs(node): ''',self.guard44,self.act44))
        self.__names['''if dfs(node): '''] = ('''if dfs(node): ''',self.guard44,self.act44)
        self.__actionClass['''if dfs(node): '''] = '''                if dfs(node): '''
        self.__orderings['''if dfs(node): '''] = 45
        self.__okExcepts['''if dfs(node): '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard45,self.act45))
        self.__names['''return True '''] = ('''return True ''',self.guard45,self.act45)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 46
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard46,self.act46))
        self.__names['''return False '''] = ('''return False ''',self.guard46,self.act46)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 47
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''def is_cyclic_undirected(self): ''',self.guard47,self.act47))
        self.__names['''def is_cyclic_undirected(self): '''] = ('''def is_cyclic_undirected(self): ''',self.guard47,self.act47)
        self.__actionClass['''def is_cyclic_undirected(self): '''] = '''    def is_cyclic_undirected(self): '''
        self.__orderings['''def is_cyclic_undirected(self): '''] = 48
        self.__okExcepts['''def is_cyclic_undirected(self): '''] = ''''''
        
        self.__actions.append(('''"""Detect if there is a cycle in an undirected graph using DFS.""" ''',self.guard48,self.act48))
        self.__names['''"""Detect if there is a cycle in an undirected graph using DFS.""" '''] = ('''"""Detect if there is a cycle in an undirected graph using DFS.""" ''',self.guard48,self.act48)
        self.__actionClass['''"""Detect if there is a cycle in an undirected graph using DFS.""" '''] = '''        """Detect if there is a cycle in an undirected graph using DFS.""" '''
        self.__orderings['''"""Detect if there is a cycle in an undirected graph using DFS.""" '''] = 49
        self.__okExcepts['''"""Detect if there is a cycle in an undirected graph using DFS.""" '''] = ''''''
        
        self.__actions.append(('''visited = [False] * self.vertices ''',self.guard49,self.act49))
        self.__names['''visited = [False] * self.vertices '''] = ('''visited = [False] * self.vertices ''',self.guard49,self.act49)
        self.__actionClass['''visited = [False] * self.vertices '''] = '''        visited = [False] * self.vertices '''
        self.__orderings['''visited = [False] * self.vertices '''] = 50
        self.__okExcepts['''visited = [False] * self.vertices '''] = ''''''
        
        self.__actions.append(('''def dfs(v, parent): ''',self.guard50,self.act50))
        self.__names['''def dfs(v, parent): '''] = ('''def dfs(v, parent): ''',self.guard50,self.act50)
        self.__actionClass['''def dfs(v, parent): '''] = '''        def dfs(v, parent): '''
        self.__orderings['''def dfs(v, parent): '''] = 51
        self.__okExcepts['''def dfs(v, parent): '''] = ''''''
        
        self.__actions.append(('''visited[v] = True ''',self.guard51,self.act51))
        self.__names['''visited[v] = True '''] = ('''visited[v] = True ''',self.guard51,self.act51)
        self.__actionClass['''visited[v] = True '''] = '''            visited[v] = True '''
        self.__orderings['''visited[v] = True '''] = 52
        self.__okExcepts['''visited[v] = True '''] = ''''''
        
        self.__actions.append(('''for neighbor, _ in self.adj_list[v]: ''',self.guard52,self.act52))
        self.__names['''for neighbor, _ in self.adj_list[v]: '''] = ('''for neighbor, _ in self.adj_list[v]: ''',self.guard52,self.act52)
        self.__actionClass['''for neighbor, _ in self.adj_list[v]: '''] = '''            for neighbor, _ in self.adj_list[v]: '''
        self.__orderings['''for neighbor, _ in self.adj_list[v]: '''] = 53
        self.__okExcepts['''for neighbor, _ in self.adj_list[v]: '''] = ''''''
        
        self.__actions.append(('''if not visited[neighbor]: ''',self.guard53,self.act53))
        self.__names['''if not visited[neighbor]: '''] = ('''if not visited[neighbor]: ''',self.guard53,self.act53)
        self.__actionClass['''if not visited[neighbor]: '''] = '''                if not visited[neighbor]: '''
        self.__orderings['''if not visited[neighbor]: '''] = 54
        self.__okExcepts['''if not visited[neighbor]: '''] = ''''''
        
        self.__actions.append(('''if dfs(neighbor, v): ''',self.guard54,self.act54))
        self.__names['''if dfs(neighbor, v): '''] = ('''if dfs(neighbor, v): ''',self.guard54,self.act54)
        self.__actionClass['''if dfs(neighbor, v): '''] = '''                    if dfs(neighbor, v): '''
        self.__orderings['''if dfs(neighbor, v): '''] = 55
        self.__okExcepts['''if dfs(neighbor, v): '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard55,self.act55))
        self.__names['''return True '''] = ('''return True ''',self.guard55,self.act55)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 56
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''elif parent != neighbor: ''',self.guard56,self.act56))
        self.__names['''elif parent != neighbor: '''] = ('''elif parent != neighbor: ''',self.guard56,self.act56)
        self.__actionClass['''elif parent != neighbor: '''] = '''                elif parent != neighbor: '''
        self.__orderings['''elif parent != neighbor: '''] = 57
        self.__okExcepts['''elif parent != neighbor: '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard57,self.act57))
        self.__names['''return True '''] = ('''return True ''',self.guard57,self.act57)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 58
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard58,self.act58))
        self.__names['''return False '''] = ('''return False ''',self.guard58,self.act58)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 59
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''for node in range(self.vertices): ''',self.guard59,self.act59))
        self.__names['''for node in range(self.vertices): '''] = ('''for node in range(self.vertices): ''',self.guard59,self.act59)
        self.__actionClass['''for node in range(self.vertices): '''] = '''        for node in range(self.vertices): '''
        self.__orderings['''for node in range(self.vertices): '''] = 60
        self.__okExcepts['''for node in range(self.vertices): '''] = ''''''
        
        self.__actions.append(('''if not visited[node]: ''',self.guard60,self.act60))
        self.__names['''if not visited[node]: '''] = ('''if not visited[node]: ''',self.guard60,self.act60)
        self.__actionClass['''if not visited[node]: '''] = '''            if not visited[node]: '''
        self.__orderings['''if not visited[node]: '''] = 61
        self.__okExcepts['''if not visited[node]: '''] = ''''''
        
        self.__actions.append(('''if dfs(node, -1): ''',self.guard61,self.act61))
        self.__names['''if dfs(node, -1): '''] = ('''if dfs(node, -1): ''',self.guard61,self.act61)
        self.__actionClass['''if dfs(node, -1): '''] = '''                if dfs(node, -1): '''
        self.__orderings['''if dfs(node, -1): '''] = 62
        self.__okExcepts['''if dfs(node, -1): '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard62,self.act62))
        self.__names['''return True '''] = ('''return True ''',self.guard62,self.act62)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 63
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard63,self.act63))
        self.__names['''return False '''] = ('''return False ''',self.guard63,self.act63)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 64
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''def is_negative_cycle(self): ''',self.guard64,self.act64))
        self.__names['''def is_negative_cycle(self): '''] = ('''def is_negative_cycle(self): ''',self.guard64,self.act64)
        self.__actionClass['''def is_negative_cycle(self): '''] = '''    def is_negative_cycle(self): '''
        self.__orderings['''def is_negative_cycle(self): '''] = 65
        self.__okExcepts['''def is_negative_cycle(self): '''] = ''''''
        
        self.__actions.append(('''"""Detect if there is a negative cycle using Bellman-Ford.""" ''',self.guard65,self.act65))
        self.__names['''"""Detect if there is a negative cycle using Bellman-Ford.""" '''] = ('''"""Detect if there is a negative cycle using Bellman-Ford.""" ''',self.guard65,self.act65)
        self.__actionClass['''"""Detect if there is a negative cycle using Bellman-Ford.""" '''] = '''        """Detect if there is a negative cycle using Bellman-Ford.""" '''
        self.__orderings['''"""Detect if there is a negative cycle using Bellman-Ford.""" '''] = 66
        self.__okExcepts['''"""Detect if there is a negative cycle using Bellman-Ford.""" '''] = ''''''
        
        self.__actions.append(('''dist = [float("inf")] * self.vertices ''',self.guard66,self.act66))
        self.__names['''dist = [float("inf")] * self.vertices '''] = ('''dist = [float("inf")] * self.vertices ''',self.guard66,self.act66)
        self.__actionClass['''dist = [float("inf")] * self.vertices '''] = '''        dist = [float("inf")] * self.vertices '''
        self.__orderings['''dist = [float("inf")] * self.vertices '''] = 67
        self.__okExcepts['''dist = [float("inf")] * self.vertices '''] = ''''''
        
        self.__actions.append(('''dist[0] = 0  # Start from node 0 ''',self.guard67,self.act67))
        self.__names['''dist[0] = 0  # Start from node 0 '''] = ('''dist[0] = 0  # Start from node 0 ''',self.guard67,self.act67)
        self.__actionClass['''dist[0] = 0  # Start from node 0 '''] = '''        dist[0] = 0  # Start from node 0 '''
        self.__orderings['''dist[0] = 0  # Start from node 0 '''] = 68
        self.__okExcepts['''dist[0] = 0  # Start from node 0 '''] = ''''''
        
        self.__actions.append(('''for _ in range(self.vertices - 1): ''',self.guard68,self.act68))
        self.__names['''for _ in range(self.vertices - 1): '''] = ('''for _ in range(self.vertices - 1): ''',self.guard68,self.act68)
        self.__actionClass['''for _ in range(self.vertices - 1): '''] = '''        for _ in range(self.vertices - 1): '''
        self.__orderings['''for _ in range(self.vertices - 1): '''] = 69
        self.__okExcepts['''for _ in range(self.vertices - 1): '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in self.edges: ''',self.guard69,self.act69))
        self.__names['''for u, v, weight in self.edges: '''] = ('''for u, v, weight in self.edges: ''',self.guard69,self.act69)
        self.__actionClass['''for u, v, weight in self.edges: '''] = '''        for u, v, weight in self.edges: '''
        self.__orderings['''for u, v, weight in self.edges: '''] = 70
        self.__okExcepts['''for u, v, weight in self.edges: '''] = ''''''
        
        self.__actions.append(('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard70,self.act70))
        self.__names['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = ('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard70,self.act70)
        self.__actionClass['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = '''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''
        self.__orderings['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = 71
        self.__okExcepts['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = ''''''
        
        self.__actions.append(('''dist[v] = dist[u] + weight ''',self.guard71,self.act71))
        self.__names['''dist[v] = dist[u] + weight '''] = ('''dist[v] = dist[u] + weight ''',self.guard71,self.act71)
        self.__actionClass['''dist[v] = dist[u] + weight '''] = '''                    dist[v] = dist[u] + weight '''
        self.__orderings['''dist[v] = dist[u] + weight '''] = 72
        self.__okExcepts['''dist[v] = dist[u] + weight '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in self.edges: ''',self.guard72,self.act72))
        self.__names['''for u, v, weight in self.edges: '''] = ('''for u, v, weight in self.edges: ''',self.guard72,self.act72)
        self.__actionClass['''for u, v, weight in self.edges: '''] = '''        for u, v, weight in self.edges: '''
        self.__orderings['''for u, v, weight in self.edges: '''] = 73
        self.__okExcepts['''for u, v, weight in self.edges: '''] = ''''''
        
        self.__actions.append(('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard73,self.act73))
        self.__names['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = ('''if dist[u] != float("inf") and dist[u] + weight < dist[v]: ''',self.guard73,self.act73)
        self.__actionClass['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = '''            if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''
        self.__orderings['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = 74
        self.__okExcepts['''if dist[u] != float("inf") and dist[u] + weight < dist[v]: '''] = ''''''
        
        self.__actions.append(('''return True  # Negative cycle detected ''',self.guard74,self.act74))
        self.__names['''return True  # Negative cycle detected '''] = ('''return True  # Negative cycle detected ''',self.guard74,self.act74)
        self.__actionClass['''return True  # Negative cycle detected '''] = '''                return True  # Negative cycle detected '''
        self.__orderings['''return True  # Negative cycle detected '''] = 75
        self.__okExcepts['''return True  # Negative cycle detected '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard75,self.act75))
        self.__names['''return False '''] = ('''return False ''',self.guard75,self.act75)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 76
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''def reset_graph(self): ''',self.guard76,self.act76))
        self.__names['''def reset_graph(self): '''] = ('''def reset_graph(self): ''',self.guard76,self.act76)
        self.__actionClass['''def reset_graph(self): '''] = '''    def reset_graph(self): '''
        self.__orderings['''def reset_graph(self): '''] = 77
        self.__okExcepts['''def reset_graph(self): '''] = ''''''
        
        self.__actions.append(('''"""Reset the graph to its empty state.""" ''',self.guard77,self.act77))
        self.__names['''"""Reset the graph to its empty state.""" '''] = ('''"""Reset the graph to its empty state.""" ''',self.guard77,self.act77)
        self.__actionClass['''"""Reset the graph to its empty state.""" '''] = '''        """Reset the graph to its empty state.""" '''
        self.__orderings['''"""Reset the graph to its empty state.""" '''] = 78
        self.__okExcepts['''"""Reset the graph to its empty state.""" '''] = ''''''
        
        self.__actions.append(('''self.edges = []  # Clear all edges ''',self.guard78,self.act78))
        self.__names['''self.edges = []  # Clear all edges '''] = ('''self.edges = []  # Clear all edges ''',self.guard78,self.act78)
        self.__actionClass['''self.edges = []  # Clear all edges '''] = '''        self.edges = []  # Clear all edges '''
        self.__orderings['''self.edges = []  # Clear all edges '''] = 79
        self.__okExcepts['''self.edges = []  # Clear all edges '''] = ''''''
        
        self.__actions.append(('''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex ''',self.guard79,self.act79))
        self.__names['''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''] = ('''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex ''',self.guard79,self.act79)
        self.__actionClass['''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''] = '''        self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''
        self.__orderings['''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''] = 80
        self.__okExcepts['''self.adj_list = {i: [] for i in range(self.vertices)}  # Reset adjacency list for each vertex '''] = ''''''
        
        self.__actions.append(('''def union(self, parent, u, v): ''',self.guard80,self.act80))
        self.__names['''def union(self, parent, u, v): '''] = ('''def union(self, parent, u, v): ''',self.guard80,self.act80)
        self.__actionClass['''def union(self, parent, u, v): '''] = '''    def union(self, parent, u, v): '''
        self.__orderings['''def union(self, parent, u, v): '''] = 81
        self.__okExcepts['''def union(self, parent, u, v): '''] = ''''''
        
        self.__actions.append(('''"""Union-find helper function.""" ''',self.guard81,self.act81))
        self.__names['''"""Union-find helper function.""" '''] = ('''"""Union-find helper function.""" ''',self.guard81,self.act81)
        self.__actionClass['''"""Union-find helper function.""" '''] = '''        """Union-find helper function.""" '''
        self.__orderings['''"""Union-find helper function.""" '''] = 82
        self.__okExcepts['''"""Union-find helper function.""" '''] = ''''''
        
        self.__actions.append(('''root_u = self.find_parent(parent, u) ''',self.guard82,self.act82))
        self.__names['''root_u = self.find_parent(parent, u) '''] = ('''root_u = self.find_parent(parent, u) ''',self.guard82,self.act82)
        self.__actionClass['''root_u = self.find_parent(parent, u) '''] = '''        root_u = self.find_parent(parent, u) '''
        self.__orderings['''root_u = self.find_parent(parent, u) '''] = 83
        self.__okExcepts['''root_u = self.find_parent(parent, u) '''] = ''''''
        
        self.__actions.append(('''root_v = self.find_parent(parent, v) ''',self.guard83,self.act83))
        self.__names['''root_v = self.find_parent(parent, v) '''] = ('''root_v = self.find_parent(parent, v) ''',self.guard83,self.act83)
        self.__actionClass['''root_v = self.find_parent(parent, v) '''] = '''        root_v = self.find_parent(parent, v) '''
        self.__orderings['''root_v = self.find_parent(parent, v) '''] = 84
        self.__okExcepts['''root_v = self.find_parent(parent, v) '''] = ''''''
        
        self.__actions.append(('''if root_u != root_v: ''',self.guard84,self.act84))
        self.__names['''if root_u != root_v: '''] = ('''if root_u != root_v: ''',self.guard84,self.act84)
        self.__actionClass['''if root_u != root_v: '''] = '''        if root_u != root_v: '''
        self.__orderings['''if root_u != root_v: '''] = 85
        self.__okExcepts['''if root_u != root_v: '''] = ''''''
        
        self.__actions.append(('''parent[root_u] = root_v ''',self.guard85,self.act85))
        self.__names['''parent[root_u] = root_v '''] = ('''parent[root_u] = root_v ''',self.guard85,self.act85)
        self.__actionClass['''parent[root_u] = root_v '''] = '''            parent[root_u] = root_v '''
        self.__orderings['''parent[root_u] = root_v '''] = 86
        self.__okExcepts['''parent[root_u] = root_v '''] = ''''''
        
        self.__actions.append(('''def find_parent(self, parent, v): ''',self.guard86,self.act86))
        self.__names['''def find_parent(self, parent, v): '''] = ('''def find_parent(self, parent, v): ''',self.guard86,self.act86)
        self.__actionClass['''def find_parent(self, parent, v): '''] = '''    def find_parent(self, parent, v): '''
        self.__orderings['''def find_parent(self, parent, v): '''] = 87
        self.__okExcepts['''def find_parent(self, parent, v): '''] = ''''''
        
        self.__actions.append(('''"""Find the root of the node using path compression.""" ''',self.guard87,self.act87))
        self.__names['''"""Find the root of the node using path compression.""" '''] = ('''"""Find the root of the node using path compression.""" ''',self.guard87,self.act87)
        self.__actionClass['''"""Find the root of the node using path compression.""" '''] = '''        """Find the root of the node using path compression.""" '''
        self.__orderings['''"""Find the root of the node using path compression.""" '''] = 88
        self.__okExcepts['''"""Find the root of the node using path compression.""" '''] = ''''''
        
        self.__actions.append(('''if parent[v] == -1: ''',self.guard88,self.act88))
        self.__names['''if parent[v] == -1: '''] = ('''if parent[v] == -1: ''',self.guard88,self.act88)
        self.__actionClass['''if parent[v] == -1: '''] = '''        if parent[v] == -1: '''
        self.__orderings['''if parent[v] == -1: '''] = 89
        self.__okExcepts['''if parent[v] == -1: '''] = ''''''
        
        self.__actions.append(('''return v ''',self.guard89,self.act89))
        self.__names['''return v '''] = ('''return v ''',self.guard89,self.act89)
        self.__actionClass['''return v '''] = '''            return v '''
        self.__orderings['''return v '''] = 90
        self.__okExcepts['''return v '''] = ''''''
        
        self.__actions.append(('''parent[v] = self.find_parent(parent, parent[v]) ''',self.guard90,self.act90))
        self.__names['''parent[v] = self.find_parent(parent, parent[v]) '''] = ('''parent[v] = self.find_parent(parent, parent[v]) ''',self.guard90,self.act90)
        self.__actionClass['''parent[v] = self.find_parent(parent, parent[v]) '''] = '''        parent[v] = self.find_parent(parent, parent[v]) '''
        self.__orderings['''parent[v] = self.find_parent(parent, parent[v]) '''] = 91
        self.__okExcepts['''parent[v] = self.find_parent(parent, parent[v]) '''] = ''''''
        
        self.__actions.append(('''return parent[v] ''',self.guard91,self.act91))
        self.__names['''return parent[v] '''] = ('''return parent[v] ''',self.guard91,self.act91)
        self.__actionClass['''return parent[v] '''] = '''        return parent[v] '''
        self.__orderings['''return parent[v] '''] = 92
        self.__okExcepts['''return parent[v] '''] = ''''''
        
        self.__actions.append(('''def is_cyclic_undirected_union_find(self): ''',self.guard92,self.act92))
        self.__names['''def is_cyclic_undirected_union_find(self): '''] = ('''def is_cyclic_undirected_union_find(self): ''',self.guard92,self.act92)
        self.__actionClass['''def is_cyclic_undirected_union_find(self): '''] = '''    def is_cyclic_undirected_union_find(self): '''
        self.__orderings['''def is_cyclic_undirected_union_find(self): '''] = 93
        self.__okExcepts['''def is_cyclic_undirected_union_find(self): '''] = ''''''
        
        self.__actions.append(('''"""Detect cycles in an undirected graph using Union-Find.""" ''',self.guard93,self.act93))
        self.__names['''"""Detect cycles in an undirected graph using Union-Find.""" '''] = ('''"""Detect cycles in an undirected graph using Union-Find.""" ''',self.guard93,self.act93)
        self.__actionClass['''"""Detect cycles in an undirected graph using Union-Find.""" '''] = '''        """Detect cycles in an undirected graph using Union-Find.""" '''
        self.__orderings['''"""Detect cycles in an undirected graph using Union-Find.""" '''] = 94
        self.__okExcepts['''"""Detect cycles in an undirected graph using Union-Find.""" '''] = ''''''
        
        self.__actions.append(('''parent = [-1] * self.vertices ''',self.guard94,self.act94))
        self.__names['''parent = [-1] * self.vertices '''] = ('''parent = [-1] * self.vertices ''',self.guard94,self.act94)
        self.__actionClass['''parent = [-1] * self.vertices '''] = '''        parent = [-1] * self.vertices '''
        self.__orderings['''parent = [-1] * self.vertices '''] = 95
        self.__okExcepts['''parent = [-1] * self.vertices '''] = ''''''
        
        self.__actions.append(('''for u, v, _ in self.edges: ''',self.guard95,self.act95))
        self.__names['''for u, v, _ in self.edges: '''] = ('''for u, v, _ in self.edges: ''',self.guard95,self.act95)
        self.__actionClass['''for u, v, _ in self.edges: '''] = '''        for u, v, _ in self.edges: '''
        self.__orderings['''for u, v, _ in self.edges: '''] = 96
        self.__okExcepts['''for u, v, _ in self.edges: '''] = ''''''
        
        self.__actions.append(('''x = self.find_parent(parent, u) ''',self.guard96,self.act96))
        self.__names['''x = self.find_parent(parent, u) '''] = ('''x = self.find_parent(parent, u) ''',self.guard96,self.act96)
        self.__actionClass['''x = self.find_parent(parent, u) '''] = '''            x = self.find_parent(parent, u) '''
        self.__orderings['''x = self.find_parent(parent, u) '''] = 97
        self.__okExcepts['''x = self.find_parent(parent, u) '''] = ''''''
        
        self.__actions.append(('''y = self.find_parent(parent, v) ''',self.guard97,self.act97))
        self.__names['''y = self.find_parent(parent, v) '''] = ('''y = self.find_parent(parent, v) ''',self.guard97,self.act97)
        self.__actionClass['''y = self.find_parent(parent, v) '''] = '''            y = self.find_parent(parent, v) '''
        self.__orderings['''y = self.find_parent(parent, v) '''] = 98
        self.__okExcepts['''y = self.find_parent(parent, v) '''] = ''''''
        
        self.__actions.append(('''if x == y: ''',self.guard98,self.act98))
        self.__names['''if x == y: '''] = ('''if x == y: ''',self.guard98,self.act98)
        self.__actionClass['''if x == y: '''] = '''            if x == y: '''
        self.__orderings['''if x == y: '''] = 99
        self.__okExcepts['''if x == y: '''] = ''''''
        
        self.__actions.append(('''return True ''',self.guard99,self.act99))
        self.__names['''return True '''] = ('''return True ''',self.guard99,self.act99)
        self.__actionClass['''return True '''] = '''                return True '''
        self.__orderings['''return True '''] = 100
        self.__okExcepts['''return True '''] = ''''''
        
        self.__actions.append(('''self.union(parent, x, y) ''',self.guard100,self.act100))
        self.__names['''self.union(parent, x, y) '''] = ('''self.union(parent, x, y) ''',self.guard100,self.act100)
        self.__actionClass['''self.union(parent, x, y) '''] = '''            self.union(parent, x, y) '''
        self.__orderings['''self.union(parent, x, y) '''] = 101
        self.__okExcepts['''self.union(parent, x, y) '''] = ''''''
        
        self.__actions.append(('''return False ''',self.guard101,self.act101))
        self.__names['''return False '''] = ('''return False ''',self.guard101,self.act101)
        self.__actionClass['''return False '''] = '''        return False '''
        self.__orderings['''return False '''] = 102
        self.__okExcepts['''return False '''] = ''''''
        
        self.__actions.append(('''def reset_graph_helper(self): ''',self.guard102,self.act102))
        self.__names['''def reset_graph_helper(self): '''] = ('''def reset_graph_helper(self): ''',self.guard102,self.act102)
        self.__actionClass['''def reset_graph_helper(self): '''] = '''    def reset_graph_helper(self): '''
        self.__orderings['''def reset_graph_helper(self): '''] = 103
        self.__okExcepts['''def reset_graph_helper(self): '''] = ''''''
        
        self.__actions.append(('''"""Reset the graph to an empty state for testing.""" ''',self.guard103,self.act103))
        self.__names['''"""Reset the graph to an empty state for testing.""" '''] = ('''"""Reset the graph to an empty state for testing.""" ''',self.guard103,self.act103)
        self.__actionClass['''"""Reset the graph to an empty state for testing.""" '''] = '''        """Reset the graph to an empty state for testing.""" '''
        self.__orderings['''"""Reset the graph to an empty state for testing.""" '''] = 104
        self.__okExcepts['''"""Reset the graph to an empty state for testing.""" '''] = ''''''
        
        self.__actions.append(('''self.edges = [] ''',self.guard104,self.act104))
        self.__names['''self.edges = [] '''] = ('''self.edges = [] ''',self.guard104,self.act104)
        self.__actionClass['''self.edges = [] '''] = '''        self.edges = [] '''
        self.__orderings['''self.edges = [] '''] = 105
        self.__okExcepts['''self.edges = [] '''] = ''''''
        
        self.__actions.append(('''self.adj_list = defaultdict(list) ''',self.guard105,self.act105))
        self.__names['''self.adj_list = defaultdict(list) '''] = ('''self.adj_list = defaultdict(list) ''',self.guard105,self.act105)
        self.__actionClass['''self.adj_list = defaultdict(list) '''] = '''        self.adj_list = defaultdict(list) '''
        self.__orderings['''self.adj_list = defaultdict(list) '''] = 106
        self.__okExcepts['''self.adj_list = defaultdict(list) '''] = ''''''
        
        self.__actions.append(('''def get_edges_helper(self): ''',self.guard106,self.act106))
        self.__names['''def get_edges_helper(self): '''] = ('''def get_edges_helper(self): ''',self.guard106,self.act106)
        self.__actionClass['''def get_edges_helper(self): '''] = '''    def get_edges_helper(self): '''
        self.__orderings['''def get_edges_helper(self): '''] = 107
        self.__okExcepts['''def get_edges_helper(self): '''] = ''''''
        
        self.__actions.append(('''"""Return all edges for testing.""" ''',self.guard107,self.act107))
        self.__names['''"""Return all edges for testing.""" '''] = ('''"""Return all edges for testing.""" ''',self.guard107,self.act107)
        self.__actionClass['''"""Return all edges for testing.""" '''] = '''        """Return all edges for testing.""" '''
        self.__orderings['''"""Return all edges for testing.""" '''] = 108
        self.__okExcepts['''"""Return all edges for testing.""" '''] = ''''''
        
        self.__actions.append(('''return self.edges ''',self.guard108,self.act108))
        self.__names['''return self.edges '''] = ('''return self.edges ''',self.guard108,self.act108)
        self.__actionClass['''return self.edges '''] = '''        return self.edges '''
        self.__orderings['''return self.edges '''] = 109
        self.__okExcepts['''return self.edges '''] = ''''''
        
        self.__actions.append(('''def add_multiple_edges_helper(self, edges): ''',self.guard109,self.act109))
        self.__names['''def add_multiple_edges_helper(self, edges): '''] = ('''def add_multiple_edges_helper(self, edges): ''',self.guard109,self.act109)
        self.__actionClass['''def add_multiple_edges_helper(self, edges): '''] = '''    def add_multiple_edges_helper(self, edges): '''
        self.__orderings['''def add_multiple_edges_helper(self, edges): '''] = 110
        self.__okExcepts['''def add_multiple_edges_helper(self, edges): '''] = ''''''
        
        self.__actions.append(('''"""Add multiple edges for testing.""" ''',self.guard110,self.act110))
        self.__names['''"""Add multiple edges for testing.""" '''] = ('''"""Add multiple edges for testing.""" ''',self.guard110,self.act110)
        self.__actionClass['''"""Add multiple edges for testing.""" '''] = '''        """Add multiple edges for testing.""" '''
        self.__orderings['''"""Add multiple edges for testing.""" '''] = 111
        self.__okExcepts['''"""Add multiple edges for testing.""" '''] = ''''''
        
        self.__actions.append(('''for edge in edges: ''',self.guard111,self.act111))
        self.__names['''for edge in edges: '''] = ('''for edge in edges: ''',self.guard111,self.act111)
        self.__actionClass['''for edge in edges: '''] = '''        for edge in edges: '''
        self.__orderings['''for edge in edges: '''] = 112
        self.__okExcepts['''for edge in edges: '''] = ''''''
        
        self.__actions.append(('''self.add_edge(*edge) ''',self.guard112,self.act112))
        self.__names['''self.add_edge(*edge) '''] = ('''self.add_edge(*edge) ''',self.guard112,self.act112)
        self.__actionClass['''self.add_edge(*edge) '''] = '''            self.add_edge(*edge) '''
        self.__orderings['''self.add_edge(*edge) '''] = 113
        self.__okExcepts['''self.add_edge(*edge) '''] = ''''''
        
        self.__actions.append(('''class CycleDetectionResults: ''',self.guard113,self.act113))
        self.__names['''class CycleDetectionResults: '''] = ('''class CycleDetectionResults: ''',self.guard113,self.act113)
        self.__actionClass['''class CycleDetectionResults: '''] = '''class CycleDetectionResults: '''
        self.__orderings['''class CycleDetectionResults: '''] = 114
        self.__okExcepts['''class CycleDetectionResults: '''] = ''''''
        
        self.__actions.append(('''def __init__(self): ''',self.guard114,self.act114))
        self.__names['''def __init__(self): '''] = ('''def __init__(self): ''',self.guard114,self.act114)
        self.__actionClass['''def __init__(self): '''] = '''    def __init__(self): '''
        self.__orderings['''def __init__(self): '''] = 115
        self.__okExcepts['''def __init__(self): '''] = ''''''
        
        self.__actions.append(('''self.directed_cycle_detected = False ''',self.guard115,self.act115))
        self.__names['''self.directed_cycle_detected = False '''] = ('''self.directed_cycle_detected = False ''',self.guard115,self.act115)
        self.__actionClass['''self.directed_cycle_detected = False '''] = '''        self.directed_cycle_detected = False '''
        self.__orderings['''self.directed_cycle_detected = False '''] = 116
        self.__okExcepts['''self.directed_cycle_detected = False '''] = ''''''
        
        self.__actions.append(('''self.undirected_cycle_detected = False ''',self.guard116,self.act116))
        self.__names['''self.undirected_cycle_detected = False '''] = ('''self.undirected_cycle_detected = False ''',self.guard116,self.act116)
        self.__actionClass['''self.undirected_cycle_detected = False '''] = '''        self.undirected_cycle_detected = False '''
        self.__orderings['''self.undirected_cycle_detected = False '''] = 117
        self.__okExcepts['''self.undirected_cycle_detected = False '''] = ''''''
        
        self.__actions.append(('''self.negative_cycle_detected = False ''',self.guard117,self.act117))
        self.__names['''self.negative_cycle_detected = False '''] = ('''self.negative_cycle_detected = False ''',self.guard117,self.act117)
        self.__actionClass['''self.negative_cycle_detected = False '''] = '''        self.negative_cycle_detected = False '''
        self.__orderings['''self.negative_cycle_detected = False '''] = 118
        self.__okExcepts['''self.negative_cycle_detected = False '''] = ''''''
        
        self.__actions.append(('''class GraphRenderer: ''',self.guard118,self.act118))
        self.__names['''class GraphRenderer: '''] = ('''class GraphRenderer: ''',self.guard118,self.act118)
        self.__actionClass['''class GraphRenderer: '''] = '''class GraphRenderer: '''
        self.__orderings['''class GraphRenderer: '''] = 119
        self.__okExcepts['''class GraphRenderer: '''] = ''''''
        
        self.__actions.append(('''def __init__(self, graph): ''',self.guard119,self.act119))
        self.__names['''def __init__(self, graph): '''] = ('''def __init__(self, graph): ''',self.guard119,self.act119)
        self.__actionClass['''def __init__(self, graph): '''] = '''    def __init__(self, graph): '''
        self.__orderings['''def __init__(self, graph): '''] = 120
        self.__okExcepts['''def __init__(self, graph): '''] = ''''''
        
        self.__actions.append(('''"""Initialize the renderer for visualizing the graph.""" ''',self.guard120,self.act120))
        self.__names['''"""Initialize the renderer for visualizing the graph.""" '''] = ('''"""Initialize the renderer for visualizing the graph.""" ''',self.guard120,self.act120)
        self.__actionClass['''"""Initialize the renderer for visualizing the graph.""" '''] = '''        """Initialize the renderer for visualizing the graph.""" '''
        self.__orderings['''"""Initialize the renderer for visualizing the graph.""" '''] = 121
        self.__okExcepts['''"""Initialize the renderer for visualizing the graph.""" '''] = ''''''
        
        self.__actions.append(('''self.graph = graph ''',self.guard121,self.act121))
        self.__names['''self.graph = graph '''] = ('''self.graph = graph ''',self.guard121,self.act121)
        self.__actionClass['''self.graph = graph '''] = '''        self.graph = graph '''
        self.__orderings['''self.graph = graph '''] = 122
        self.__okExcepts['''self.graph = graph '''] = ''''''
        
        self.__actions.append(('''def render_edges(self): ''',self.guard122,self.act122))
        self.__names['''def render_edges(self): '''] = ('''def render_edges(self): ''',self.guard122,self.act122)
        self.__actionClass['''def render_edges(self): '''] = '''    def render_edges(self): '''
        self.__orderings['''def render_edges(self): '''] = 123
        self.__okExcepts['''def render_edges(self): '''] = ''''''
        
        self.__actions.append(('''"""Render the edges of the graph.""" ''',self.guard123,self.act123))
        self.__names['''"""Render the edges of the graph.""" '''] = ('''"""Render the edges of the graph.""" ''',self.guard123,self.act123)
        self.__actionClass['''"""Render the edges of the graph.""" '''] = '''        """Render the edges of the graph.""" '''
        self.__orderings['''"""Render the edges of the graph.""" '''] = 124
        self.__okExcepts['''"""Render the edges of the graph.""" '''] = ''''''
        
        self.__actions.append(('''print("\nRendering edges of the graph:") ''',self.guard124,self.act124))
        self.__names['''print("\nRendering edges of the graph:") '''] = ('''print("\nRendering edges of the graph:") ''',self.guard124,self.act124)
        self.__actionClass['''print("\nRendering edges of the graph:") '''] = '''        print("\nRendering edges of the graph:") '''
        self.__orderings['''print("\nRendering edges of the graph:") '''] = 125
        self.__okExcepts['''print("\nRendering edges of the graph:") '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in self.graph.get_edges(): ''',self.guard125,self.act125))
        self.__names['''for u, v, weight in self.graph.get_edges(): '''] = ('''for u, v, weight in self.graph.get_edges(): ''',self.guard125,self.act125)
        self.__actionClass['''for u, v, weight in self.graph.get_edges(): '''] = '''        for u, v, weight in self.graph.get_edges(): '''
        self.__orderings['''for u, v, weight in self.graph.get_edges(): '''] = 126
        self.__okExcepts['''for u, v, weight in self.graph.get_edges(): '''] = ''''''
        
        self.__actions.append(('''{v} (Weight: {weight})") ''',self.guard126,self.act126))
        self.__names['''{v} (Weight: {weight})") '''] = ('''{v} (Weight: {weight})") ''',self.guard126,self.act126)
        self.__actionClass['''{v} (Weight: {weight})") '''] = '''            print(f"{u} -> {v} (Weight: {weight})") '''
        self.__orderings['''{v} (Weight: {weight})") '''] = 127
        self.__okExcepts['''{v} (Weight: {weight})") '''] = ''''''
        
        self.__actions.append(('''def render_adj_list(self): ''',self.guard127,self.act127))
        self.__names['''def render_adj_list(self): '''] = ('''def render_adj_list(self): ''',self.guard127,self.act127)
        self.__actionClass['''def render_adj_list(self): '''] = '''    def render_adj_list(self): '''
        self.__orderings['''def render_adj_list(self): '''] = 128
        self.__okExcepts['''def render_adj_list(self): '''] = ''''''
        
        self.__actions.append(('''"""Render the adjacency list of the graph.""" ''',self.guard128,self.act128))
        self.__names['''"""Render the adjacency list of the graph.""" '''] = ('''"""Render the adjacency list of the graph.""" ''',self.guard128,self.act128)
        self.__actionClass['''"""Render the adjacency list of the graph.""" '''] = '''        """Render the adjacency list of the graph.""" '''
        self.__orderings['''"""Render the adjacency list of the graph.""" '''] = 129
        self.__okExcepts['''"""Render the adjacency list of the graph.""" '''] = ''''''
        
        self.__actions.append(('''print("\nRendering adjacency list:") ''',self.guard129,self.act129))
        self.__names['''print("\nRendering adjacency list:") '''] = ('''print("\nRendering adjacency list:") ''',self.guard129,self.act129)
        self.__actionClass['''print("\nRendering adjacency list:") '''] = '''        print("\nRendering adjacency list:") '''
        self.__orderings['''print("\nRendering adjacency list:") '''] = 130
        self.__okExcepts['''print("\nRendering adjacency list:") '''] = ''''''
        
        self.__actions.append(('''self.graph.print_adj_list() ''',self.guard130,self.act130))
        self.__names['''self.graph.print_adj_list() '''] = ('''self.graph.print_adj_list() ''',self.guard130,self.act130)
        self.__actionClass['''self.graph.print_adj_list() '''] = '''        self.graph.print_adj_list() '''
        self.__orderings['''self.graph.print_adj_list() '''] = 131
        self.__okExcepts['''self.graph.print_adj_list() '''] = ''''''
        
        self.__actions.append(('''def render_summary(self): ''',self.guard131,self.act131))
        self.__names['''def render_summary(self): '''] = ('''def render_summary(self): ''',self.guard131,self.act131)
        self.__actionClass['''def render_summary(self): '''] = '''    def render_summary(self): '''
        self.__orderings['''def render_summary(self): '''] = 132
        self.__okExcepts['''def render_summary(self): '''] = ''''''
        
        self.__actions.append(('''"""Render a summary of the graph.""" ''',self.guard132,self.act132))
        self.__names['''"""Render a summary of the graph.""" '''] = ('''"""Render a summary of the graph.""" ''',self.guard132,self.act132)
        self.__actionClass['''"""Render a summary of the graph.""" '''] = '''        """Render a summary of the graph.""" '''
        self.__orderings['''"""Render a summary of the graph.""" '''] = 133
        self.__okExcepts['''"""Render a summary of the graph.""" '''] = ''''''
        
        self.__actions.append(('''print("\nGraph summary:") ''',self.guard133,self.act133))
        self.__names['''print("\nGraph summary:") '''] = ('''print("\nGraph summary:") ''',self.guard133,self.act133)
        self.__actionClass['''print("\nGraph summary:") '''] = '''        print("\nGraph summary:") '''
        self.__orderings['''print("\nGraph summary:") '''] = 134
        self.__okExcepts['''print("\nGraph summary:") '''] = ''''''
        
        self.__actions.append(('''print(f"Total vertices: {self.graph.vertices}") ''',self.guard134,self.act134))
        self.__names['''print(f"Total vertices: {self.graph.vertices}") '''] = ('''print(f"Total vertices: {self.graph.vertices}") ''',self.guard134,self.act134)
        self.__actionClass['''print(f"Total vertices: {self.graph.vertices}") '''] = '''        print(f"Total vertices: {self.graph.vertices}") '''
        self.__orderings['''print(f"Total vertices: {self.graph.vertices}") '''] = 135
        self.__okExcepts['''print(f"Total vertices: {self.graph.vertices}") '''] = ''''''
        
        self.__actions.append(('''print(f"Total edges: {len(self.graph.get_edges())}") ''',self.guard135,self.act135))
        self.__names['''print(f"Total edges: {len(self.graph.get_edges())}") '''] = ('''print(f"Total edges: {len(self.graph.get_edges())}") ''',self.guard135,self.act135)
        self.__actionClass['''print(f"Total edges: {len(self.graph.get_edges())}") '''] = '''        print(f"Total edges: {len(self.graph.get_edges())}") '''
        self.__orderings['''print(f"Total edges: {len(self.graph.get_edges())}") '''] = 136
        self.__okExcepts['''print(f"Total edges: {len(self.graph.get_edges())}") '''] = ''''''
        
        self.__actions.append(('''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") ''',self.guard136,self.act136))
        self.__names['''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''] = ('''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") ''',self.guard136,self.act136)
        self.__actionClass['''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''] = '''        print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''
        self.__orderings['''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''] = 137
        self.__okExcepts['''print(f"Is cyclic (directed): {self.graph.is_cyclic_directed()}") '''] = ''''''
        
        self.__actions.append(('''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") ''',self.guard137,self.act137))
        self.__names['''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''] = ('''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") ''',self.guard137,self.act137)
        self.__actionClass['''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''] = '''        print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''
        self.__orderings['''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''] = 138
        self.__okExcepts['''print(f"Is cyclic (undirected): {self.graph.is_cyclic_undirected()}") '''] = ''''''
        
        self.__actions.append(('''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") ''',self.guard138,self.act138))
        self.__names['''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''] = ('''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") ''',self.guard138,self.act138)
        self.__actionClass['''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''] = '''        print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''
        self.__orderings['''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''] = 139
        self.__okExcepts['''print(f"Has negative cycle: {self.graph.is_negative_cycle()}") '''] = ''''''
        
        self.__actions.append(('''import matplotlib.pyplot as plt ''',self.guard139,self.act139))
        self.__names['''import matplotlib.pyplot as plt '''] = ('''import matplotlib.pyplot as plt ''',self.guard139,self.act139)
        self.__actionClass['''import matplotlib.pyplot as plt '''] = '''import matplotlib.pyplot as plt '''
        self.__orderings['''import matplotlib.pyplot as plt '''] = 140
        self.__okExcepts['''import matplotlib.pyplot as plt '''] = ''''''
        
        self.__actions.append(('''import networkx as nx ''',self.guard140,self.act140))
        self.__names['''import networkx as nx '''] = ('''import networkx as nx ''',self.guard140,self.act140)
        self.__actionClass['''import networkx as nx '''] = '''import networkx as nx '''
        self.__orderings['''import networkx as nx '''] = 141
        self.__okExcepts['''import networkx as nx '''] = ''''''
        
        self.__actions.append(('''class WeightedGraphVisualization: ''',self.guard141,self.act141))
        self.__names['''class WeightedGraphVisualization: '''] = ('''class WeightedGraphVisualization: ''',self.guard141,self.act141)
        self.__actionClass['''class WeightedGraphVisualization: '''] = '''class WeightedGraphVisualization: '''
        self.__orderings['''class WeightedGraphVisualization: '''] = 142
        self.__okExcepts['''class WeightedGraphVisualization: '''] = ''''''
        
        self.__actions.append(('''def __init__(self, graph): ''',self.guard142,self.act142))
        self.__names['''def __init__(self, graph): '''] = ('''def __init__(self, graph): ''',self.guard142,self.act142)
        self.__actionClass['''def __init__(self, graph): '''] = '''    def __init__(self, graph): '''
        self.__orderings['''def __init__(self, graph): '''] = 143
        self.__okExcepts['''def __init__(self, graph): '''] = ''''''
        
        self.__actions.append(('''"""Initialize the visualization of weighted graph.""" ''',self.guard143,self.act143))
        self.__names['''"""Initialize the visualization of weighted graph.""" '''] = ('''"""Initialize the visualization of weighted graph.""" ''',self.guard143,self.act143)
        self.__actionClass['''"""Initialize the visualization of weighted graph.""" '''] = '''        """Initialize the visualization of weighted graph.""" '''
        self.__orderings['''"""Initialize the visualization of weighted graph.""" '''] = 144
        self.__okExcepts['''"""Initialize the visualization of weighted graph.""" '''] = ''''''
        
        self.__actions.append(('''self.graph = graph ''',self.guard144,self.act144))
        self.__names['''self.graph = graph '''] = ('''self.graph = graph ''',self.guard144,self.act144)
        self.__actionClass['''self.graph = graph '''] = '''        self.graph = graph '''
        self.__orderings['''self.graph = graph '''] = 145
        self.__okExcepts['''self.graph = graph '''] = ''''''
        
        self.__actions.append(('''def visualize(self): ''',self.guard145,self.act145))
        self.__names['''def visualize(self): '''] = ('''def visualize(self): ''',self.guard145,self.act145)
        self.__actionClass['''def visualize(self): '''] = '''    def visualize(self): '''
        self.__orderings['''def visualize(self): '''] = 146
        self.__okExcepts['''def visualize(self): '''] = ''''''
        
        self.__actions.append(('''"""Visualize the graph with weighted edges using networkx and matplotlib.""" ''',self.guard146,self.act146))
        self.__names['''"""Visualize the graph with weighted edges using networkx and matplotlib.""" '''] = ('''"""Visualize the graph with weighted edges using networkx and matplotlib.""" ''',self.guard146,self.act146)
        self.__actionClass['''"""Visualize the graph with weighted edges using networkx and matplotlib.""" '''] = '''        """Visualize the graph with weighted edges using networkx and matplotlib.""" '''
        self.__orderings['''"""Visualize the graph with weighted edges using networkx and matplotlib.""" '''] = 147
        self.__okExcepts['''"""Visualize the graph with weighted edges using networkx and matplotlib.""" '''] = ''''''
        
        self.__actions.append(('''G = nx.DiGraph()  # Using DiGraph for directed graph visualization ''',self.guard147,self.act147))
        self.__names['''G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''] = ('''G = nx.DiGraph()  # Using DiGraph for directed graph visualization ''',self.guard147,self.act147)
        self.__actionClass['''G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''] = '''        G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''
        self.__orderings['''G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''] = 148
        self.__okExcepts['''G = nx.DiGraph()  # Using DiGraph for directed graph visualization '''] = ''''''
        
        self.__actions.append(('''for u, v, weight in self.graph.get_edges(): ''',self.guard148,self.act148))
        self.__names['''for u, v, weight in self.graph.get_edges(): '''] = ('''for u, v, weight in self.graph.get_edges(): ''',self.guard148,self.act148)
        self.__actionClass['''for u, v, weight in self.graph.get_edges(): '''] = '''        for u, v, weight in self.graph.get_edges(): '''
        self.__orderings['''for u, v, weight in self.graph.get_edges(): '''] = 149
        self.__okExcepts['''for u, v, weight in self.graph.get_edges(): '''] = ''''''
        
        self.__actions.append(('''G.add_edge(u, v, weight=weight) ''',self.guard149,self.act149))
        self.__names['''G.add_edge(u, v, weight=weight) '''] = ('''G.add_edge(u, v, weight=weight) ''',self.guard149,self.act149)
        self.__actionClass['''G.add_edge(u, v, weight=weight) '''] = '''            G.add_edge(u, v, weight=weight) '''
        self.__orderings['''G.add_edge(u, v, weight=weight) '''] = 150
        self.__okExcepts['''G.add_edge(u, v, weight=weight) '''] = ''''''
        
        self.__actions.append(('''pos = nx.spring_layout(G)  # Layout for node positioning ''',self.guard150,self.act150))
        self.__names['''pos = nx.spring_layout(G)  # Layout for node positioning '''] = ('''pos = nx.spring_layout(G)  # Layout for node positioning ''',self.guard150,self.act150)
        self.__actionClass['''pos = nx.spring_layout(G)  # Layout for node positioning '''] = '''        pos = nx.spring_layout(G)  # Layout for node positioning '''
        self.__orderings['''pos = nx.spring_layout(G)  # Layout for node positioning '''] = 151
        self.__okExcepts['''pos = nx.spring_layout(G)  # Layout for node positioning '''] = ''''''
        
        self.__actions.append(('''edge_labels = nx.get_edge_attributes(G, 'weight') ''',self.guard151,self.act151))
        self.__names['''edge_labels = nx.get_edge_attributes(G, 'weight') '''] = ('''edge_labels = nx.get_edge_attributes(G, 'weight') ''',self.guard151,self.act151)
        self.__actionClass['''edge_labels = nx.get_edge_attributes(G, 'weight') '''] = '''        edge_labels = nx.get_edge_attributes(G, 'weight') '''
        self.__orderings['''edge_labels = nx.get_edge_attributes(G, 'weight') '''] = 152
        self.__okExcepts['''edge_labels = nx.get_edge_attributes(G, 'weight') '''] = ''''''
        
        self.__actions.append(('''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') ''',self.guard152,self.act152))
        self.__names['''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''] = ('''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') ''',self.guard152,self.act152)
        self.__actionClass['''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''] = '''        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''
        self.__orderings['''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''] = 153
        self.__okExcepts['''nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=12, font_weight='bold') '''] = ''''''
        
        self.__actions.append(('''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) ''',self.guard153,self.act153))
        self.__names['''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''] = ('''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) ''',self.guard153,self.act153)
        self.__actionClass['''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''] = '''        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''
        self.__orderings['''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''] = 154
        self.__okExcepts['''nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels) '''] = ''''''
        
        self.__actions.append(('''plt.title("Graph Visualization with Weighted Edges") ''',self.guard154,self.act154))
        self.__names['''plt.title("Graph Visualization with Weighted Edges") '''] = ('''plt.title("Graph Visualization with Weighted Edges") ''',self.guard154,self.act154)
        self.__actionClass['''plt.title("Graph Visualization with Weighted Edges") '''] = '''        plt.title("Graph Visualization with Weighted Edges") '''
        self.__orderings['''plt.title("Graph Visualization with Weighted Edges") '''] = 155
        self.__okExcepts['''plt.title("Graph Visualization with Weighted Edges") '''] = ''''''
        
        self.__actions.append(('''plt.show() ''',self.guard155,self.act155))
        self.__names['''plt.show() '''] = ('''plt.show() ''',self.guard155,self.act155)
        self.__actionClass['''plt.show() '''] = '''        plt.show() '''
        self.__orderings['''plt.show() '''] = 156
        self.__okExcepts['''plt.show() '''] = ''''''
        
        self.__actions.append(('''class WeightedGraphHandler: ''',self.guard156,self.act156))
        self.__names['''class WeightedGraphHandler: '''] = ('''class WeightedGraphHandler: ''',self.guard156,self.act156)
        self.__actionClass['''class WeightedGraphHandler: '''] = '''class WeightedGraphHandler: '''
        self.__orderings['''class WeightedGraphHandler: '''] = 157
        self.__okExcepts['''class WeightedGraphHandler: '''] = ''''''
        
        self.__actions.append(('''def __init__(self, vertices): ''',self.guard157,self.act157))
        self.__names['''def __init__(self, vertices): '''] = ('''def __init__(self, vertices): ''',self.guard157,self.act157)
        self.__actionClass['''def __init__(self, vertices): '''] = '''    def __init__(self, vertices): '''
        self.__orderings['''def __init__(self, vertices): '''] = 158
        self.__okExcepts['''def __init__(self, vertices): '''] = ''''''
        
        self.__actions.append(('''"""Initialize the graph handler.""" ''',self.guard158,self.act158))
        self.__names['''"""Initialize the graph handler.""" '''] = ('''"""Initialize the graph handler.""" ''',self.guard158,self.act158)
        self.__actionClass['''"""Initialize the graph handler.""" '''] = '''        """Initialize the graph handler.""" '''
        self.__orderings['''"""Initialize the graph handler.""" '''] = 159
        self.__okExcepts['''"""Initialize the graph handler.""" '''] = ''''''
        
        self.__actions.append(('''self.graph = WeightedGraph(vertices) ''',self.guard159,self.act159))
        self.__names['''self.graph = WeightedGraph(vertices) '''] = ('''self.graph = WeightedGraph(vertices) ''',self.guard159,self.act159)
        self.__actionClass['''self.graph = WeightedGraph(vertices) '''] = '''        self.graph = WeightedGraph(vertices) '''
        self.__orderings['''self.graph = WeightedGraph(vertices) '''] = 160
        self.__okExcepts['''self.graph = WeightedGraph(vertices) '''] = ''''''
        
        self.__actions.append(('''self.renderer = GraphRenderer(self.graph) ''',self.guard160,self.act160))
        self.__names['''self.renderer = GraphRenderer(self.graph) '''] = ('''self.renderer = GraphRenderer(self.graph) ''',self.guard160,self.act160)
        self.__actionClass['''self.renderer = GraphRenderer(self.graph) '''] = '''        self.renderer = GraphRenderer(self.graph) '''
        self.__orderings['''self.renderer = GraphRenderer(self.graph) '''] = 161
        self.__okExcepts['''self.renderer = GraphRenderer(self.graph) '''] = ''''''
        
        self.__actions.append(('''self.visualizer = WeightedGraphVisualization(self.graph) ''',self.guard161,self.act161))
        self.__names['''self.visualizer = WeightedGraphVisualization(self.graph) '''] = ('''self.visualizer = WeightedGraphVisualization(self.graph) ''',self.guard161,self.act161)
        self.__actionClass['''self.visualizer = WeightedGraphVisualization(self.graph) '''] = '''        self.visualizer = WeightedGraphVisualization(self.graph) '''
        self.__orderings['''self.visualizer = WeightedGraphVisualization(self.graph) '''] = 162
        self.__okExcepts['''self.visualizer = WeightedGraphVisualization(self.graph) '''] = ''''''
        
        self.__actions.append(('''def add_edges(self, edges): ''',self.guard162,self.act162))
        self.__names['''def add_edges(self, edges): '''] = ('''def add_edges(self, edges): ''',self.guard162,self.act162)
        self.__actionClass['''def add_edges(self, edges): '''] = '''    def add_edges(self, edges): '''
        self.__orderings['''def add_edges(self, edges): '''] = 163
        self.__okExcepts['''def add_edges(self, edges): '''] = ''''''
        
        self.__actions.append(('''"""Add edges to the graph.""" ''',self.guard163,self.act163))
        self.__names['''"""Add edges to the graph.""" '''] = ('''"""Add edges to the graph.""" ''',self.guard163,self.act163)
        self.__actionClass['''"""Add edges to the graph.""" '''] = '''        """Add edges to the graph.""" '''
        self.__orderings['''"""Add edges to the graph.""" '''] = 164
        self.__okExcepts['''"""Add edges to the graph.""" '''] = ''''''
        
        self.__actions.append(('''for edge in edges: ''',self.guard164,self.act164))
        self.__names['''for edge in edges: '''] = ('''for edge in edges: ''',self.guard164,self.act164)
        self.__actionClass['''for edge in edges: '''] = '''        for edge in edges: '''
        self.__orderings['''for edge in edges: '''] = 165
        self.__okExcepts['''for edge in edges: '''] = ''''''
        
        self.__actions.append(('''self.graph.add_edge(*edge) ''',self.guard165,self.act165))
        self.__names['''self.graph.add_edge(*edge) '''] = ('''self.graph.add_edge(*edge) ''',self.guard165,self.act165)
        self.__actionClass['''self.graph.add_edge(*edge) '''] = '''            self.graph.add_edge(*edge) '''
        self.__orderings['''self.graph.add_edge(*edge) '''] = 166
        self.__okExcepts['''self.graph.add_edge(*edge) '''] = ''''''
        
        self.__actions.append(('''def render_graph(self): ''',self.guard166,self.act166))
        self.__names['''def render_graph(self): '''] = ('''def render_graph(self): ''',self.guard166,self.act166)
        self.__actionClass['''def render_graph(self): '''] = '''    def render_graph(self): '''
        self.__orderings['''def render_graph(self): '''] = 167
        self.__okExcepts['''def render_graph(self): '''] = ''''''
        
        self.__actions.append(('''"""Render the graph using the renderer.""" ''',self.guard167,self.act167))
        self.__names['''"""Render the graph using the renderer.""" '''] = ('''"""Render the graph using the renderer.""" ''',self.guard167,self.act167)
        self.__actionClass['''"""Render the graph using the renderer.""" '''] = '''        """Render the graph using the renderer.""" '''
        self.__orderings['''"""Render the graph using the renderer.""" '''] = 168
        self.__okExcepts['''"""Render the graph using the renderer.""" '''] = ''''''
        
        self.__actions.append(('''self.renderer.render_edges() ''',self.guard168,self.act168))
        self.__names['''self.renderer.render_edges() '''] = ('''self.renderer.render_edges() ''',self.guard168,self.act168)
        self.__actionClass['''self.renderer.render_edges() '''] = '''        self.renderer.render_edges() '''
        self.__orderings['''self.renderer.render_edges() '''] = 169
        self.__okExcepts['''self.renderer.render_edges() '''] = ''''''
        
        self.__actions.append(('''self.renderer.render_adj_list() ''',self.guard169,self.act169))
        self.__names['''self.renderer.render_adj_list() '''] = ('''self.renderer.render_adj_list() ''',self.guard169,self.act169)
        self.__actionClass['''self.renderer.render_adj_list() '''] = '''        self.renderer.render_adj_list() '''
        self.__orderings['''self.renderer.render_adj_list() '''] = 170
        self.__okExcepts['''self.renderer.render_adj_list() '''] = ''''''
        
        self.__actions.append(('''def visualize_graph(self): ''',self.guard170,self.act170))
        self.__names['''def visualize_graph(self): '''] = ('''def visualize_graph(self): ''',self.guard170,self.act170)
        self.__actionClass['''def visualize_graph(self): '''] = '''    def visualize_graph(self): '''
        self.__orderings['''def visualize_graph(self): '''] = 171
        self.__okExcepts['''def visualize_graph(self): '''] = ''''''
        
        self.__actions.append(('''"""Visualize the graph using the visualizer.""" ''',self.guard171,self.act171))
        self.__names['''"""Visualize the graph using the visualizer.""" '''] = ('''"""Visualize the graph using the visualizer.""" ''',self.guard171,self.act171)
        self.__actionClass['''"""Visualize the graph using the visualizer.""" '''] = '''        """Visualize the graph using the visualizer.""" '''
        self.__orderings['''"""Visualize the graph using the visualizer.""" '''] = 172
        self.__okExcepts['''"""Visualize the graph using the visualizer.""" '''] = ''''''
        
        self.__actions.append(('''self.visualizer.visualize() ''',self.guard172,self.act172))
        self.__names['''self.visualizer.visualize() '''] = ('''self.visualizer.visualize() ''',self.guard172,self.act172)
        self.__actionClass['''self.visualizer.visualize() '''] = '''        self.visualizer.visualize() '''
        self.__orderings['''self.visualizer.visualize() '''] = 173
        self.__okExcepts['''self.visualizer.visualize() '''] = ''''''
        
        self.__actions.append(('''def cycle_detection_summary(self): ''',self.guard173,self.act173))
        self.__names['''def cycle_detection_summary(self): '''] = ('''def cycle_detection_summary(self): ''',self.guard173,self.act173)
        self.__actionClass['''def cycle_detection_summary(self): '''] = '''    def cycle_detection_summary(self): '''
        self.__orderings['''def cycle_detection_summary(self): '''] = 174
        self.__okExcepts['''def cycle_detection_summary(self): '''] = ''''''
        
        self.__actions.append(('''"""Print the cycle detection summary.""" ''',self.guard174,self.act174))
        self.__names['''"""Print the cycle detection summary.""" '''] = ('''"""Print the cycle detection summary.""" ''',self.guard174,self.act174)
        self.__actionClass['''"""Print the cycle detection summary.""" '''] = '''        """Print the cycle detection summary.""" '''
        self.__orderings['''"""Print the cycle detection summary.""" '''] = 175
        self.__okExcepts['''"""Print the cycle detection summary.""" '''] = ''''''
        
        self.__actions.append(('''print("\nCycle detection summary:") ''',self.guard175,self.act175))
        self.__names['''print("\nCycle detection summary:") '''] = ('''print("\nCycle detection summary:") ''',self.guard175,self.act175)
        self.__actionClass['''print("\nCycle detection summary:") '''] = '''        print("\nCycle detection summary:") '''
        self.__orderings['''print("\nCycle detection summary:") '''] = 176
        self.__okExcepts['''print("\nCycle detection summary:") '''] = ''''''
        
        self.__actions.append(('''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") ''',self.guard176,self.act176))
        self.__names['''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''] = ('''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") ''',self.guard176,self.act176)
        self.__actionClass['''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''] = '''        print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''
        self.__orderings['''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''] = 177
        self.__okExcepts['''print(f"Directed cycle detected: {self.graph.is_cyclic_directed()}") '''] = ''''''
        
        self.__actions.append(('''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") ''',self.guard177,self.act177))
        self.__names['''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''] = ('''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") ''',self.guard177,self.act177)
        self.__actionClass['''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''] = '''        print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''
        self.__orderings['''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''] = 178
        self.__okExcepts['''print(f"Undirected cycle detected: {self.graph.is_cyclic_undirected()}") '''] = ''''''
        
        self.__actions.append(('''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") ''',self.guard178,self.act178))
        self.__names['''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''] = ('''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") ''',self.guard178,self.act178)
        self.__actionClass['''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''] = '''        print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''
        self.__orderings['''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''] = 179
        self.__okExcepts['''print(f"Negative cycle detected: {self.graph.is_negative_cycle()}") '''] = ''''''
        
        self.__actions.append(('''class GraphCycleAnalysis: ''',self.guard179,self.act179))
        self.__names['''class GraphCycleAnalysis: '''] = ('''class GraphCycleAnalysis: ''',self.guard179,self.act179)
        self.__actionClass['''class GraphCycleAnalysis: '''] = '''class GraphCycleAnalysis: '''
        self.__orderings['''class GraphCycleAnalysis: '''] = 180
        self.__okExcepts['''class GraphCycleAnalysis: '''] = ''''''
        
        self.__actions.append(('''def __init__(self, graph): ''',self.guard180,self.act180))
        self.__names['''def __init__(self, graph): '''] = ('''def __init__(self, graph): ''',self.guard180,self.act180)
        self.__actionClass['''def __init__(self, graph): '''] = '''    def __init__(self, graph): '''
        self.__orderings['''def __init__(self, graph): '''] = 181
        self.__okExcepts['''def __init__(self, graph): '''] = ''''''
        
        self.__actions.append(('''"""Initialize cycle analysis on the graph.""" ''',self.guard181,self.act181))
        self.__names['''"""Initialize cycle analysis on the graph.""" '''] = ('''"""Initialize cycle analysis on the graph.""" ''',self.guard181,self.act181)
        self.__actionClass['''"""Initialize cycle analysis on the graph.""" '''] = '''        """Initialize cycle analysis on the graph.""" '''
        self.__orderings['''"""Initialize cycle analysis on the graph.""" '''] = 182
        self.__okExcepts['''"""Initialize cycle analysis on the graph.""" '''] = ''''''
        
        self.__actions.append(('''self.graph = graph ''',self.guard182,self.act182))
        self.__names['''self.graph = graph '''] = ('''self.graph = graph ''',self.guard182,self.act182)
        self.__actionClass['''self.graph = graph '''] = '''        self.graph = graph '''
        self.__orderings['''self.graph = graph '''] = 183
        self.__okExcepts['''self.graph = graph '''] = ''''''
        
        self.__actions.append(('''self.results = CycleDetectionResults() ''',self.guard183,self.act183))
        self.__names['''self.results = CycleDetectionResults() '''] = ('''self.results = CycleDetectionResults() ''',self.guard183,self.act183)
        self.__actionClass['''self.results = CycleDetectionResults() '''] = '''        self.results = CycleDetectionResults() '''
        self.__orderings['''self.results = CycleDetectionResults() '''] = 184
        self.__okExcepts['''self.results = CycleDetectionResults() '''] = ''''''
        
        self.__actions.append(('''def analyze_cycles(self): ''',self.guard184,self.act184))
        self.__names['''def analyze_cycles(self): '''] = ('''def analyze_cycles(self): ''',self.guard184,self.act184)
        self.__actionClass['''def analyze_cycles(self): '''] = '''    def analyze_cycles(self): '''
        self.__orderings['''def analyze_cycles(self): '''] = 185
        self.__okExcepts['''def analyze_cycles(self): '''] = ''''''
        
        self.__actions.append(('''"""Analyze different types of cycles in the graph.""" ''',self.guard185,self.act185))
        self.__names['''"""Analyze different types of cycles in the graph.""" '''] = ('''"""Analyze different types of cycles in the graph.""" ''',self.guard185,self.act185)
        self.__actionClass['''"""Analyze different types of cycles in the graph.""" '''] = '''        """Analyze different types of cycles in the graph.""" '''
        self.__orderings['''"""Analyze different types of cycles in the graph.""" '''] = 186
        self.__okExcepts['''"""Analyze different types of cycles in the graph.""" '''] = ''''''
        
        self.__actions.append(('''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() ''',self.guard186,self.act186))
        self.__names['''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''] = ('''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() ''',self.guard186,self.act186)
        self.__actionClass['''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''] = '''        self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''
        self.__orderings['''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''] = 187
        self.__okExcepts['''self.results.directed_cycle_detected = self.graph.is_cyclic_directed() '''] = ''''''
        
        self.__actions.append(('''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() ''',self.guard187,self.act187))
        self.__names['''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''] = ('''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() ''',self.guard187,self.act187)
        self.__actionClass['''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''] = '''        self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''
        self.__orderings['''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''] = 188
        self.__okExcepts['''self.results.undirected_cycle_detected = self.graph.is_cyclic_undirected() '''] = ''''''
        
        self.__actions.append(('''self.results.negative_cycle_detected = self.graph.is_negative_cycle() ''',self.guard188,self.act188))
        self.__names['''self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''] = ('''self.results.negative_cycle_detected = self.graph.is_negative_cycle() ''',self.guard188,self.act188)
        self.__actionClass['''self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''] = '''        self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''
        self.__orderings['''self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''] = 189
        self.__okExcepts['''self.results.negative_cycle_detected = self.graph.is_negative_cycle() '''] = ''''''
        
        self.__actions.append(('''def print_analysis(self): ''',self.guard189,self.act189))
        self.__names['''def print_analysis(self): '''] = ('''def print_analysis(self): ''',self.guard189,self.act189)
        self.__actionClass['''def print_analysis(self): '''] = '''    def print_analysis(self): '''
        self.__orderings['''def print_analysis(self): '''] = 190
        self.__okExcepts['''def print_analysis(self): '''] = ''''''
        
        self.__actions.append(('''"""Print the analysis results.""" ''',self.guard190,self.act190))
        self.__names['''"""Print the analysis results.""" '''] = ('''"""Print the analysis results.""" ''',self.guard190,self.act190)
        self.__actionClass['''"""Print the analysis results.""" '''] = '''        """Print the analysis results.""" '''
        self.__orderings['''"""Print the analysis results.""" '''] = 191
        self.__okExcepts['''"""Print the analysis results.""" '''] = ''''''
        
        self.__actions.append(('''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") ''',self.guard191,self.act191))
        self.__names['''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''] = ('''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") ''',self.guard191,self.act191)
        self.__actionClass['''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''] = '''        print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''
        self.__orderings['''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''] = 192
        self.__okExcepts['''print(f"Directed cycle detected: {self.results.directed_cycle_detected}") '''] = ''''''
        
        self.__actions.append(('''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") ''',self.guard192,self.act192))
        self.__names['''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''] = ('''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") ''',self.guard192,self.act192)
        self.__actionClass['''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''] = '''        print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''
        self.__orderings['''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''] = 193
        self.__okExcepts['''print(f"Undirected cycle detected: {self.results.undirected_cycle_detected}") '''] = ''''''
        
        self.__actions.append(('''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") ''',self.guard193,self.act193))
        self.__names['''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''] = ('''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") ''',self.guard193,self.act193)
        self.__actionClass['''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''] = '''        print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''
        self.__orderings['''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''] = 194
        self.__okExcepts['''print(f"Negative cycle detected: {self.results.negative_cycle_detected}") '''] = ''''''
        
        self.__actions.append(('''if __name__ == "__main__": ''',self.guard194,self.act194))
        self.__names['''if __name__ == "__main__": '''] = ('''if __name__ == "__main__": ''',self.guard194,self.act194)
        self.__actionClass['''if __name__ == "__main__": '''] = '''if __name__ == "__main__": '''
        self.__orderings['''if __name__ == "__main__": '''] = 195
        self.__okExcepts['''if __name__ == "__main__": '''] = ''''''
        
        self.__actions.append(('''graph_handler = WeightedGraphHandler(4) ''',self.guard195,self.act195))
        self.__names['''graph_handler = WeightedGraphHandler(4) '''] = ('''graph_handler = WeightedGraphHandler(4) ''',self.guard195,self.act195)
        self.__actionClass['''graph_handler = WeightedGraphHandler(4) '''] = '''    graph_handler = WeightedGraphHandler(4) '''
        self.__orderings['''graph_handler = WeightedGraphHandler(4) '''] = 196
        self.__okExcepts['''graph_handler = WeightedGraphHandler(4) '''] = ''''''
        
        self.__actions.append(('''edges = [ ''',self.guard196,self.act196))
        self.__names['''edges = [ '''] = ('''edges = [ ''',self.guard196,self.act196)
        self.__actionClass['''edges = [ '''] = '''    edges = [ '''
        self.__orderings['''edges = [ '''] = 197
        self.__okExcepts['''edges = [ '''] = ''''''
        
        self.__actions.append(('''(0, 1, 10),  # Edge from 0 to 1 with weight 10 ''',self.guard197,self.act197))
        self.__names['''(0, 1, 10),  # Edge from 0 to 1 with weight 10 '''] = ('''(0, 1, 10),  # Edge from 0 to 1 with weight 10 ''',self.guard197,self.act197)
        self.__actionClass['''(0, 1, 10),  # Edge from 0 to 1 with weight 10 '''] = '''        (0, 1, 10),  # Edge from 0 to 1 with weight 10 '''
        self.__orderings['''(0, 1, 10),  # Edge from 0 to 1 with weight 10 '''] = 198
        self.__okExcepts['''(0, 1, 10),  # Edge from 0 to 1 with weight 10 '''] = ''''''
        
        self.__actions.append(('''(1, 2, 20),  # Edge from 1 to 2 with weight 20 ''',self.guard198,self.act198))
        self.__names['''(1, 2, 20),  # Edge from 1 to 2 with weight 20 '''] = ('''(1, 2, 20),  # Edge from 1 to 2 with weight 20 ''',self.guard198,self.act198)
        self.__actionClass['''(1, 2, 20),  # Edge from 1 to 2 with weight 20 '''] = '''        (1, 2, 20),  # Edge from 1 to 2 with weight 20 '''
        self.__orderings['''(1, 2, 20),  # Edge from 1 to 2 with weight 20 '''] = 199
        self.__okExcepts['''(1, 2, 20),  # Edge from 1 to 2 with weight 20 '''] = ''''''
        
        self.__actions.append(('''(2, 3, 30),  # Edge from 2 to 3 with weight 30 ''',self.guard199,self.act199))
        self.__names['''(2, 3, 30),  # Edge from 2 to 3 with weight 30 '''] = ('''(2, 3, 30),  # Edge from 2 to 3 with weight 30 ''',self.guard199,self.act199)
        self.__actionClass['''(2, 3, 30),  # Edge from 2 to 3 with weight 30 '''] = '''        (2, 3, 30),  # Edge from 2 to 3 with weight 30 '''
        self.__orderings['''(2, 3, 30),  # Edge from 2 to 3 with weight 30 '''] = 200
        self.__okExcepts['''(2, 3, 30),  # Edge from 2 to 3 with weight 30 '''] = ''''''
        
        self.__actions.append((''' ''',self.guard200,self.act200))
        self.__names[''' '''] = (''' ''',self.guard200,self.act200)
        self.__actionClass[''' '''] = '''        (3, 0, 40),  # Edge from 3 to 0 with weight 40 (creates a directed cycle: 0 -> 1 -> 2 -> 3 -> 0) '''
        self.__orderings[''' '''] = 201
        self.__okExcepts[''' '''] = ''''''
        
        self.__actions.append(('''(0, 2, 50)  # Edge from 0 to 2 with weight 50 ''',self.guard201,self.act201))
        self.__names['''(0, 2, 50)  # Edge from 0 to 2 with weight 50 '''] = ('''(0, 2, 50)  # Edge from 0 to 2 with weight 50 ''',self.guard201,self.act201)
        self.__actionClass['''(0, 2, 50)  # Edge from 0 to 2 with weight 50 '''] = '''        (0, 2, 50)  # Edge from 0 to 2 with weight 50 '''
        self.__orderings['''(0, 2, 50)  # Edge from 0 to 2 with weight 50 '''] = 202
        self.__okExcepts['''(0, 2, 50)  # Edge from 0 to 2 with weight 50 '''] = ''''''
        
        self.__actions.append(('''] ''',self.guard202,self.act202))
        self.__names['''] '''] = ('''] ''',self.guard202,self.act202)
        self.__actionClass['''] '''] = '''    ] '''
        self.__orderings['''] '''] = 203
        self.__okExcepts['''] '''] = ''''''
        
        self.__actions.append(('''graph_handler.add_edges(edges) ''',self.guard203,self.act203))
        self.__names['''graph_handler.add_edges(edges) '''] = ('''graph_handler.add_edges(edges) ''',self.guard203,self.act203)
        self.__actionClass['''graph_handler.add_edges(edges) '''] = '''    graph_handler.add_edges(edges) '''
        self.__orderings['''graph_handler.add_edges(edges) '''] = 204
        self.__okExcepts['''graph_handler.add_edges(edges) '''] = ''''''
        
        self.__actions.append(('''graph_handler.render_graph() ''',self.guard204,self.act204))
        self.__names['''graph_handler.render_graph() '''] = ('''graph_handler.render_graph() ''',self.guard204,self.act204)
        self.__actionClass['''graph_handler.render_graph() '''] = '''    graph_handler.render_graph() '''
        self.__orderings['''graph_handler.render_graph() '''] = 205
        self.__okExcepts['''graph_handler.render_graph() '''] = ''''''
        
        self.__actions.append(('''graph_handler.visualize_graph() ''',self.guard205,self.act205))
        self.__names['''graph_handler.visualize_graph() '''] = ('''graph_handler.visualize_graph() ''',self.guard205,self.act205)
        self.__actionClass['''graph_handler.visualize_graph() '''] = '''    graph_handler.visualize_graph() '''
        self.__orderings['''graph_handler.visualize_graph() '''] = 206
        self.__okExcepts['''graph_handler.visualize_graph() '''] = ''''''
        
        self.__actions.append(('''graph_handler.cycle_detection_summary() ''',self.guard206,self.act206))
        self.__names['''graph_handler.cycle_detection_summary() '''] = ('''graph_handler.cycle_detection_summary() ''',self.guard206,self.act206)
        self.__actionClass['''graph_handler.cycle_detection_summary() '''] = '''    graph_handler.cycle_detection_summary() '''
        self.__orderings['''graph_handler.cycle_detection_summary() '''] = 207
        self.__okExcepts['''graph_handler.cycle_detection_summary() '''] = ''''''
        
        self.__actions.append(('''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) ''',self.guard207,self.act207))
        self.__names['''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''] = ('''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) ''',self.guard207,self.act207)
        self.__actionClass['''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''] = '''    cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''
        self.__orderings['''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''] = 208
        self.__okExcepts['''cycle_analysis = GraphCycleAnalysis(graph_handler.graph) '''] = ''''''
        
        self.__actions.append(('''cycle_analysis.analyze_cycles() ''',self.guard208,self.act208))
        self.__names['''cycle_analysis.analyze_cycles() '''] = ('''cycle_analysis.analyze_cycles() ''',self.guard208,self.act208)
        self.__actionClass['''cycle_analysis.analyze_cycles() '''] = '''    cycle_analysis.analyze_cycles() '''
        self.__orderings['''cycle_analysis.analyze_cycles() '''] = 209
        self.__okExcepts['''cycle_analysis.analyze_cycles() '''] = ''''''
        
        self.__actions.append(('''cycle_analysis.print_analysis() ''',self.guard209,self.act209))
        self.__names['''cycle_analysis.print_analysis() '''] = ('''cycle_analysis.print_analysis() ''',self.guard209,self.act209)
        self.__actionClass['''cycle_analysis.print_analysis() '''] = '''    cycle_analysis.print_analysis() '''
        self.__orderings['''cycle_analysis.print_analysis() '''] = 210
        self.__okExcepts['''cycle_analysis.print_analysis() '''] = ''''''
        self.__actions_backup = list(self.__actions)
        self.__actions_assume_backup = list(self.__actions)
    def slowPoolStates(self):
        nonePools = []
        notUsedPools = []
        return (nonePools, notUsedPools)
    def restart(self):
        try:
            test_before_restart(self)
        except:
            pass
        if self.__collectCov: self.cleanCov()
    # BEGIN RELOAD CODE
    # END RELOAD CODE
        self.__test = []
        self.__failure = None
        self.__warning = None
        self.__raised = None
        self.__refRaised = None
        self.__poolsNone = set([])
        self.__poolsUsed = set([])
        self.__disabledByNone = set([])
        self.__disabledByUsed = set([])
        if self.__useCould: self.computeInitialEnabled()
        try:
            test_after_restart(self)
        except:
            pass
    def hints(self):
        return []
    def log(self, name):
        pass
    def logPost(self, name):
        pass
    def state(self):
        if self.__replayBacktrack:
            return self.captureReplay(self.__test)
        st = []
        st.append(copy.copy(self.__test))
        return st
    def shallowState(self):
        return []
    def abstract(self,state):
        if self.__replayBacktrack:
            return state
        return ()
    def backtrack(self,old):
        if self.__replayBacktrack:
            self.replay(self.replayable(old))
            return
        self.__test = copy.copy(old[-1])
    def check(self):
        return True
    """
    BOILERPLATE METHODS OF SUT
    ==========================
    These are the set of methods available on each SUT by default
    
    Examples
    --------
    
    t.enabled()
    t.actions()
    """
    
    
    def setReplayBacktrack(self, val):
        self.__replayBacktrack = val
    
    
    def test(self):
        """
        Returns the current test as a sequence of (name, guard, actions)
        """
        return self.__test
    
    
    def SUTName(self):
        return self.__SUTName
    
    
    def raised(self):
        """
        Returns exception raised by last action, or None if no exception was raised
        """
        return self.__raised
    
    
    def refRaised(self):
        """
        Returns exception raised by last reference action, or None if no exception was raised
        """
        return self.__refRaised
    
    
    def getOkExceptions(self, name):
        return self.__okExcepts[name]
    
    
    def getPreCode(self, name):
        try:
            return self.__preCode[name]
        except BaseException:
            return None
    
    
    def getRefCode(self, name):
        try:
            return self.__refCode[name]
        except BaseException:
            return None
    
    
    def getPropCode(self, name):
        try:
            return self.__propCode[name]
        except BaseException:
            return None
    
    
    def actionClass(self, action):
        return self.__actionClass[action[0]]
    
    
    def dependencies(self, actClass):
        return self.__dependencies[actClass]
    
    
    def abstraction(self, pool):
        if pool not in self.__abstraction:
            return None
        return self.__abstraction[pool]
    
    
    def prettyName(self, name):
        newName = name
        for p in self.__pools:
            pfind = newName.find(p + "[")
            while pfind != -1:
                closePos = newName.find("]", pfind)
                index = newName[newName.find("[", pfind) + 1:closePos]
                access = newName[pfind:newName.find("]", pfind) + 1]
                needUnderscore = ""
                if p[-1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    needUnderscore = "_"
                newAccess = p.replace(self.__poolPrefix, "") + \
                    needUnderscore + index
                newName = newName.replace(access, newAccess)
                pfind = newName.find(p + "[")
        return newName
    
    
    def actOrder(self, action):
        return self.__orderings[action[0]]
    
    
    def pools(self):
        return self.__pools
    
    
    def prettyPrintTest(self, test, columns=80):
        i = 0
        for a in test:
            s = a[0]
            steps = "# STEP " + str(i)
            if len(a) > 3:  # NOW ALLOW ANNOTATIONS!
                steps += "  ;;; " + a[3]
            print(self.prettyName(s).ljust(columns - len(steps), ' '), steps)
            i += 1
    
    
    def prettyPrintRemoved(self, test1, test2, columns=80):
        # Assumption is that test2 is test1 with parts removed!
        i = 0
        j = 0
        for a in test1:
            s = a[0]
            if i < len(test2):
                sdiff = test2[i][0]
            else:
                sdiff = None
            if s != sdiff:
                steps = ""
                if len(a) > 3:  # NOW ALLOW ANNOTATIONS!
                    steps += "  ;;; " + a[3]
                print(self.prettyName(s).ljust(columns - len(steps), ' '), steps)
                j += 1
            else:
                i += 1
                j = i
    
    
    def exploreFromHere(self, depth, checkProp=True, stopFail=True, stopCover=False,
                        gatherFail=None, gatherCover=None, verbose=False, reverse=False,
                        visited=None):
        """
        Does a DFS complete exploration.  Recursive, so limited depth, but deep runs
        unlikely to be useful, anyway.
        """
        state = self.state()
    
        if visited is not None:
            if type(visited) == list:
                if state[:-1] in visited:
                    if verbose == "BACKTRACK":
                        print("BACKTRACKING DUE TO ALREADY VISITED STATE:",
                              state[:-1])
                    return True
                else:
                    visited.append(state[:-1])
            elif type(visited) == dict:
                rs = repr(state[:-1])
                if rs in visited:
                    if verbose == "BACKTRACK":
                        print("BACKTRACKING DUE TO ALREADY VISITED STATE",
                              rs)
                    return True
                else:
                    visited[rs] = True
    
        acts = self.enabled()
        if reverse:
            # More interesting actions tend to be later in order
            acts.reverse()
    
        for a in acts:
            if verbose == "STEPS":
                print(depth, a[0])
            ok = self.safely(a)
            if not ok:
                if stopFail:
                    if verbose:
                        print("TEST FAILED!")
                    return False
                elif gatherFail is not None:
                    if verbose:
                        print("NEW FAILING TEST OF LENGTH", len(self.test()))
                        f = self.failure()
                        print("FAILURE ON ACTION:", self.prettyName(a[0]))
                        print("ERROR:", f)
                        traceback.print_tb(f[2], file=sys.stdout)
                    gatherFail.append(list(self.test()))
            if checkProp:
                if not self.check():
                    if stopFail:
                        if verbose:
                            print("PROPERTY CHECK FAILED!")
                        return False
                    elif gatherFail is not None:
                        if verbose:
                            print("NEW FAILING TEST OF LENGTH", len(self.test()))
                        f = self.failure()
                        print("FAILED PROPERTY CHECK ON ACTION:", self.prettyName(a[0]))
                        print("ERROR:", f)
                        traceback.print_tb(f[2], file=sys.stdout)
                        gatherFail.append(list(self.test()))
            if (len(self.newBranches()) > 0) or (len(self.newStatements()) > 0):
                if stopCover:
                    return False
                elif gatherCover is not None:
                    if verbose:
                        print("COLLECTED TEST WITH NEW COVERAGE FROM ACTION",
                              self.prettyName(a[0]))
                        print("ADDED", len(self.newBranches()), "BRANCHES AND",
                              len(self.newStatements()), "STATEMENTS")
                    gatherCover.append(list(self.test()))
            if depth > 1:
                r = self.exploreFromHere(depth - 1, checkProp, stopFail, stopCover,
                                         gatherFail, gatherCover, verbose, reverse,
                                         visited)
                if not r:
                    return r
            try:
                self.backtrack(state)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                print("WARNING: FAILURE IN INITIAL EXPLORATION PATH")
        return True
    
    
    def getPoolStates(self):
        if self.__useCould and not self.__actionCould:
            return (self.__poolsNone, self.__poolsUsed)
        else:
            return self.slowPoolStates()
    
    
    def setUseDependencies(self, value):
        self.__useCould = value
    
    
    def setActionApproximation(self, value):
        self.__actionCould = value
    
    
    def setFastPoolStates(self, value):
        self.__fastPoolStates = value
    
    
    def captureReplay(self, test):
        captured = ""
        for step in test:
            captured += self.serializable(step)
            captured += "#!#!"
        return captured[:-4]
    
    
    def replayable(self, stest):
        steps = stest.split("#!#!")
        if steps == ['']:
            return []
        return list(map(self.playable, steps))
    
    
    def enabled(self):
        """
        Returns all enabled action objects.
        """
        if self.__useCould:
            acts = self.couldBeEnabled()
        else:
            acts = self.__actions
        return [s_g_a1 for s_g_a1 in acts if s_g_a1[1]()]
    
    
    def couldBeEnabled(self):
        couldBe = set(map(lambda x: x[0], self.__actions))
        if self.__actionCould:
            if self.verboseActionCould:
                print("couldBe:", len(couldBe))
                print("NONE:", len(self.__disabledByNone))
                print("USED:", len(self.__disabledByUsed))
            couldBe -= self.__disabledByNone
            couldBe -= self.__disabledByUsed
            if self.verboseActionCould:
                print("couldBe:", len(couldBe))
        else:
            pNone, pNotUsed = self.getPoolStates()
            for p in pNone:
                if p in self.__poolUsers:
                    for a in self.__poolUsers[p]:
                        couldBe.discard(a)
            if self.__relaxUsedRestriction:
                return map(lambda x: self.__names[x], couldBe)
            for p in pNotUsed:
                if p in self.__poolInitializers:
                    for a in self.__poolInitializers[p]:
                        if p not in pNone:
                            couldBe.discard(a)
        return map(lambda x: self.__names[x], couldBe)
    
    
    def nowUsed(self, pool):
        if self.__actionCould:
            if pool in self.__poolInitializers:
                for a in self.__poolInitializers[pool]:
                    if self.verboseActionCould:
                        print("ENABLING", a, "DUE TO NOW USED POOL", pool)
                    self.__disabledByUsed.discard(a)
        else:
            self.__poolsUsed.add(pool)
    
    
    def noLongerNone(self, pool):
        if self.__actionCould:
            if pool in self.__poolUsers:
                for a in self.__poolUsers[pool]:
                    if self.verboseActionCould:
                        print("ENABLING", a, "DUE TO ASSIGNING TO POOL", pool)
                        print("IN DISABLED BY USED POOL?", a in self.__disabledByUsed)
                        print("OLD LENGTH", len(self.__disabledByNone))
                    self.__disabledByNone.discard(a)
                    if self.verboseActionCould:
                        print("NEW LENGTH", len(self.__disabledByNone))
        else:
            self.__poolsNone.discard(pool)
    
    
    def noLongerUsed(self, pool):
        if self.__actionCould:
            if pool in self.__poolInitializers:
                for a in self.__poolInitializers[pool]:
                    if self.verboseActionCould:
                        print("DISABLING", a, "DUE TO NO LONGER USED POOL", pool)
                    self.__disabledByUsed.add(a)
        else:
            self.__poolsUsed.discard(pool)
    
    
    def computeInitialEnabled(self):
        pNone, pNotUsed = self.slowPoolStates()
        for p in pNone:
            if self.__actionCould:
                if p in self.__poolUsers:
                    for a in self.__poolUsers[p]:
                        self.__disabledByNone.add(a)
            else:
                self.__poolsNone.add(p)
    
    
    def highLowSwarm(self, rgen, P=0.5, file=None, highProb=0.9, noDependencies=False, forceParent=True):
        high = []
    
        if file is not None:
            classProb = {}
            for l in open(file):
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
    
        for c in self.__actionClasses:
            if file is None:
                if rgen.random() < P:
                    high.append(c)
            else:
                if rgen.random() < classProb[c]:
                    high.append(c)
        if high == []:
            high.append(rgen.choice(self.__actionClasses))
    
        changed = True
        if noDependencies:
            changed = False
    
        while changed:
            changed = False
    
            if forceParent:
                forcedAdd = []
                for c in newEnabled:
                    allParents = []
                    for pp in self.__actionClasses:
                        for dl in self.dependencies(pp):
                            if c in dl:
                                allParents.append(pp)
                                break
                    if allParents == []:
                        continue
                    anyParents = [x for x in newEnabled if x in allParents]
                    anyParents.extend([x for x in forcedAdd if x in allParents])
                    if anyParents == []:
                        addC = rgen.choice(allParents)
                        forcedAdd.append(addC)
                        changed = True
                newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in high:
                for d in self.dependencies(c):
                    df = [x for x in high if x in d] + \
                        [x for x in forcedAdd if x in d]
                    if df == []:
                        forcedAdd.append(rgen.choice(d))
                        changed = True
            high.extend(forcedAdd)
    
            forcedAdd = []
            for c in high:
                if self.dependencies(c) == []:
                    anyDepend = False
                    for c2 in (high + forcedAdd):
                        for d in self.dependencies(c2):
                            if c in d:
                                anyDepend = True
                                break
                        if anyDepend:
                            break
                    if not anyDepend:
                        needsThis = []
                        for c2 in self.__actionClasses:
                            for d in self.dependencies(c2):
                                if c in d:
                                    needsThis.append(c2)
                                    break
                        if needsThis != []:
                            forcedAdd.append(rgen.choice(needsThis))
                            changed = True
            high.extend(forcedAdd)
        low = [x for x in self.__actionClasses if x not in high]
        probs = []
        if low == []:
            return [(1.0 / len(high), x) for x in high]
        if high == []:
            return [(1.0 / len(low), x) for x in low]
        highP = highProb / len(high)
        lowP = (1.0 - highProb) / len(low)
        for c in high:
            probs.append((highP, c))
        for c in low:
            probs.append((lowP, c))
        return probs
    
    
    def highLowClassProbs(self, rgen, P=0.5, file=None, highProb=0.9):
        high = []
        low = []
        if file is not None:
            classProb = {}
            for l in open(file):
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
    
        for c in self.__actionClasses:
            if file is None:
                if rgen.random() < P:
                    high.append(c)
                else:
                    low.append(c)
            else:
                if rgen.random() < classProb[c]:
                    high.append(c)
                else:
                    low.append(c)
        probs = []
        if low == []:
            return [(1.0 / len(high), x) for x in high]
        if high == []:
            return [(1.0 / len(low), x) for x in low]
        highP = highProb / len(high)
        lowP = (1.0 - highProb) / len(low)
        for c in high:
            probs.append((highP, c))
        for c in low:
            probs.append((lowP, c))
        return probs
    
    
    def randomEnabledClassProbs(self, rgen, probs):
        if self.__enumerateEnabled:
            enableds = self.enabled()
        else:
            enableds = None
        a = None
        while a is None:
            r = rgen.random()
            p = 0.0
            ac = None
            for (pac, tac) in probs:
                p += pac
                if p > r:
                    ac = tac
                    break
            a = self.randomEnabled(rgen, actFilter=lambda act: self.actionClass(
                act) == ac, enabledActs=enableds)
            if a is None:
                if len(probs) == 1:
                    return None
                padd = pac / (len(probs) - 1)
                newprobs = []
                for (pac, tac2) in probs:
                    if tac2 == tac:
                        continue
                    newprobs.append((pac + padd, tac2))
                probs = newprobs
                if probs == []:
                    break
        return a
    
    
    def setEnumerateEnabled(self, bval):
        self.__enumerateEnabled = bval
    
    
    def randomEnabled(self, rgen, actFilter=None, enabledActs=None):
        """
        Return a random enabled action, or None if no such action can be
        produced, based on a provided random generator.
        """
        if enabledActs is not None:
            acts = list(enabledActs)
        elif self.__useCould:
            acts = self.couldBeEnabled()
        else:
            acts = self.__actions
        if filter is not None:
            acts = list(filter(actFilter, acts))
        if self.__enumerateEnabled:
            try:
                return rgen.choice([s_g_a for s_g_a in acts if s_g_a[1]()])
            except IndexError:
                return None
        a = None
        while a is None:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                break
            else:
                a = None
            acts = acts[:p] + acts[p + 1:]
        return a
    
    
    def randomEnableds(self, rgen, n):
        """
        Return list of random enabled actions, up to n actions if possible
        """
    
        retActs = []
        acts = self.__actions
        if self.__enumerateEnabled:
            acts = self.enabled()
        while len(retActs) < n:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                retActs.append(a)
            acts = acts[:p] + acts[p + 1:]
        return retActs
    
    
    def randomEnabledPred(self, rgen, n, pred):
        """
        Return first enabled action satisfying pred, with up to n attempts.
        If none found, returns last enabled action checked.
        """
    
        tries = 0
        acts = self.__actions
        if self.__enumerateEnabled:
            acts = self.enabled()
        a = None
        lastSafe = None
        while tries < n:
            if len(acts) == 1:
                p = 0
            elif len(acts) == 0:
                break
            else:
                p = rgen.randint(0, len(acts) - 1)
            a = acts[p]
            if a[1]():
                lastSafe = a
                if pred(a):
                    return a
                tries += 1
            acts = acts[:p] + acts[p + 1:]
        return lastSafe
    
    
    def mutate(self, test, rgen, Pinsert=0.2):
        '''
        Simple tool for mutating tests randomly.  Does not ensure validity
        of the new test, which may be functionally equivalent.  There are
        two types of mutation, replacement and insertion.  Pinsert gives
        probability of insert (default 0.2).
        '''
        newTest = list(test)
        loc = rgen.randrange(0, len(test))
        act = rgen.choice(self.__actions)
        if rgen.random() < Pinsert:
            newTest.insert(loc, act)
        else:
            newTest[loc] = act
        return newTest
    
    
    def crossover(self, test1, test2, rgen, twoPoint=False):
        '''
        Simple code for performing crossover of two tests.  Just picks an
        order, then picks a point at which to stop first test then start
        second.  twoPoint results in two point crossover.
        '''
        if rgen.randrange(2) == 0:
            t1 = test1
            t2 = test2
        else:
            t2 = test1
            t1 = test2
        if len(t1) > 1:
            p1 = rgen.randrange(1, len(t1))
        else:
            p1 = 1
        if len(t2) > 0:
            p2 = rgen.randrange(0, len(t2))
        else:
            p2 = 0
        newTest = t1[:p1]
        if twoPoint:
            if len(t1) > 1:
                p3 = rgen.randrange(p1, len(t1))
            else:
                p3 = 1
            if len(t2) > 0:
                p4 = rgen.randrange(p2, len(t2))
            else:
                p4 = 0
            newTest.extend(t2[p2:p4])
            newTest.extend(t1[p3:])
        else:
            newTest.extend(t2[p2:])
        return newTest
    
    
    def makeTest(
            self,
            size,
            rgen=None,
            generator=None,
            sgenerator=None,
            stopFail=True,
            checkProp=True,
            initial=None,
            timeout=None,
            stopWhen=None):
        '''
        Allows generation of fixed length tests using either a default
        generator (pure random testing), or using a simple generator that
        only takes the current test step as input (generator) or a complex
        stateful generator (sgenerator).  An sgenerator must take as input
        both a state and an interface to the SUT (to query for coverage,
        etc.) and return an (action, new state) tuple.  User can also
        control whether to stop on failure, whether to check properties,
        and supply a timeout in seconds.
    
        '''
    
        if timeout is not None:
            stime = time.time()
    
        noFailure = True
    
        if generator is not None:
            genF = generator
        else:
            def genF(x): return self.randomEnabled(rgen)
        if sgenerator is not None:
            state = initial
        self.restart()
        for i in range(0, size):
            if stopWhen is not None:
                if stopWhen():
                    return (list(self.test()), noFailure)
            if sgenerator is None:
                action = genF(i)
                if action is None:
                    return (list(self.test()), "DEADLOCK")
                ok = self.safely(action)
            else:
                (action, state) = sgenerator(state, self)
                if action is None:
                    return (list(self.test()), "DEADLOCK")
                ok = self.safely(action)
            if not ok:
                noFailure = False
                if stopFail:
                    return (list(self.test()), False)
            if checkProp:
                if not self.check():
                    noFailure = False
                    if stopFail:
                        return (list(self.test()), False)
            if timeout is not None:
                if (time.time() - stime) > timeout:
                    return (list(self.test()), noFailure)
        return (list(self.test()), noFailure)
    
    
    def features(self):
        return self.__features
    
    
    def actions(self):
        """
        Returns all the action objects whether enabled or disabled.
        """
        return self.__actions
    
    
    def actionClasses(self):
        return self.__actionClasses
    
    
    def essentialClasses(self):
        return self.__essentialClasses
    
    
    def disable(self, f):
        """
        Disable an action by name.
        """
        newActions = []
        for a in self.__actions:
            name = a[0]
            guard = a[1]
            act = a[2]
            if not re.match(f, name):
                newActions.append((name, guard, act))
        self.__actions = newActions
    
    
    def enableAll(self):
        """
        Enable all actions.
        """
        self.__swarmConfig = None
        self.__actions = self.__actions_backup
        self.__actions_assume_backup = list(self.__actions_backup)
    
    
    def enableAllAssume(self):
        """
        Enable all actions, but restricted by current swarm set
        """
        self.__actions = self.__actions_assume_backup
    
    
    def objCodeLOCs(self, obj, context):
        LOCs = []
        for o in inspect.getmembers(obj):
            try:
                if inspect.isfunction(o[1]) or inspect.ismethod(o[1]):
                    if o[0] == "__init__":
                        LOCs.append(
                            (context[-1], len(inspect.getsourcelines(o[1])[0]), context))
                    LOCs.append(
                        (o[0], len(inspect.getsourcelines(o[1])[0]), context))
                if inspect.isclass(o[1]):
                    if o[1] == object:
                        continue
                    if o[1] == type:
                        continue
                    LOCs.extend(self.objCodeLOCs(o[1], context + [o[0]]))
            except BaseException:
                pass
        return LOCs
    
    
    def codeLOCs(self):
        LOCs = []
        for m in self.__importModules:
            LOCs.extend(self.objCodeLOCs(m, [m.__name__]))
        return LOCs
    
    
    def codeLOCProbs(self, baseline=0.2, codeLOCs=None):
        if codeLOCs is None:
            # use static estimation if no dynamic estimates provided
            cl = self.codeLOCs()
        else:
            cl = codeLOCs
    
        totalLOCs = 0.0
        aProbs = []
        num0LOC = 0
    
        for a in self.__actionClasses:
            thisLOC = 0
            for (f, LOC, c) in cl:
                if (("." + f + "(") in a):
                    thisLOC += LOC
            totalLOCs += thisLOC
            if thisLOC == 0:
                num0LOC += 1
            aProbs.append((a, thisLOC))
        P = []
        leftOver = 1.0 - baseline
        for (a, LOC) in aProbs:
            if LOC == 0:
                P.append((baseline / num0LOC, a))
            else:
                P.append(((LOC / totalLOCs) * leftOver, a))
        return P
    
    
    def writeProbFile(self, file, classProb):
        with open(file, 'w') as f:
            for ac in classProb:
                f.write(ac + " %%%% " + str(classProb[ac]) + "\n")
    
    
    def readProbFile(self, file, returnList=False):
        classProb = {}
        with open(file) as f:
            for l in f:
                ls = l.split("%%%%")
                c = ls[0][:-1]
                prob = float(ls[1])
                classProb[c] = prob
        if not returnList:
            return classProb
        pl = []
        for k in classProb:
            pl.append((classProb[k], k))
        return pl
    
    
    def standardSwarm(
            self,
            rgen,
            P=0.5,
            file=None,
            classProb=None,
            noDependencies=False,
            forceParent=True):
        """
        Enables all actions, then sets a swarm configuration based on
        rgen, P = probability of enabling an action class, file is a file
        (format action %%%% probability) giving probabilities for
        inclusion)
        """
        self.enableAll()
        newEnabled = []
    
        if file is not None:
            classProb = self.readProbFile(file)
    
        for c in self.__actionClasses:
            if classProb is None:
                if (c in self.__essentialClasses) or (rgen.random() < P):
                    newEnabled.append(c)
            else:
                if c not in classProb:
                    classProb[c] = P
                if rgen.random() < classProb[c]:
                    newEnabled.append(c)
        if newEnabled == []:
            newEnabled.append(rgen.choice(self.__actionClasses))
    
        changed = True
        if noDependencies:
            changed = False
    
        while changed:
            changed = False
    
            if forceParent:
                forcedAdd = []
                for c in newEnabled:
                    allParents = []
                    for pp in self.__actionClasses:
                        for dl in self.dependencies(pp):
                            if c in dl:
                                allParents.append(pp)
                                break
                    if allParents == []:
                        continue
                    anyParents = [x for x in newEnabled if x in allParents]
                    anyParents.extend([x for x in forcedAdd if x in allParents])
                    if anyParents == []:
                        addC = rgen.choice(allParents)
                        forcedAdd.append(addC)
                        changed = True
                newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in newEnabled:
                for d in self.dependencies(c):
                    df = [x for x in newEnabled if x in d] + \
                        [x for x in forcedAdd if x in d]
                    if df == []:
                        forcedAdd.append(rgen.choice(d))
                        changed = True
            newEnabled.extend(forcedAdd)
    
            forcedAdd = []
            for c in newEnabled:
                if self.dependencies(c) == []:
                    anyDepend = False
                    for c2 in (newEnabled + forcedAdd):
                        for d in self.dependencies(c2):
                            if c in d:
                                anyDepend = True
                                break
                        if anyDepend:
                            break
                    if not anyDepend:
                        needsThis = []
                        for c2 in self.__actionClasses:
                            for d in self.dependencies(c2):
                                if c in d:
                                    needsThis.append(c2)
                                    break
                        if needsThis != []:
                            forcedAdd.append(rgen.choice(needsThis))
                            changed = True
            newEnabled.extend(forcedAdd)
    
        self.__swarmConfig = newEnabled
        enabledActions = []
        for a in self.__actions:
            if self.actionClass(a) in newEnabled:
                enabledActions.append(a)
        self.__actions = enabledActions
        self.__actions_assume_backup = list(self.__actions)
    
    
    def swarmConfig(self):
        return self.__swarmConfig
    
    
    def serializable(self, step):
        ser = step[0]
        if len(step) > 3:
            ser += ";;;" + step[3]
        return ser
    
    
    def annotate(self, text):
        self.__test[-1] = self.__test[-1] + (text,)
    
    
    def testToBytes(self, test):
        alen = len(self.actions())
        bytes = 2
        fmt = "<H"
        if alen < 256:
            bytes = 1
            fmt = "<B"
        if alen > 2**16:
            bytes = 4
            fmt = "<L"
        data = b""
        for s in test:
            index = 0
            for a in self.actions():
                if a == s:
                    break
                index += 1
            p = struct.pack(fmt, index)
            data += p
        return data
    
    
    def saveTest(self, test, filename, afl=False):
        if not afl:
            outf = open(filename, 'w')
        else:
            outf = open(filename, 'wb')
        if not afl:
            for s in test:
                outf.write(self.serializable(s) + "\n")
        else:
            outf.write(self.testToBytes(test))
        outf.close()
    
    
    def bytesToTest(self, data, swarm=False):
        alen = len(self.actions())
        bytes = 2
        fmt = "<H"
        if alen < 256:
            bytes = 1
            fmt = "<B"
        if alen > 2**16:
            bytes = 4
            fmt = "<L"
        test = []
        if swarm:
            R = random.Random()
            seed = struct.unpack("<L", data[0:4])[0]
            R.seed(seed)
            self.standardSwarm(R)
            data = data[4:]
            alen = len(self.actions())
        for i in range(0, (len(data) // bytes)):
            index = struct.unpack(
                fmt, data[i * bytes:(i * bytes) + bytes])[0] % alen
            test.append(self.actions()[index])
        return test
    
    
    def loadTest(self, filename, afl=False, swarm=False):
        if afl:
            with open(filename, 'rb') as f:
                return self.bytesToTest(f.read(), swarm=swarm)
    
        test = []
        with open(filename) as f:
            for l in f:
                test.append(self.playable(l[:-1]))
        return test
    
    
    def playable(self, name):
        if ";;;" in name:
            annotateSplit = name.split(";;;")
            rname = annotateSplit[0]
            return self.__names[rname] + (annotateSplit[1],)
        else:
            return self.__names[name]
    
    
    def setDebugSafelyMode(self, mode):
        self.__safeSafelyMode = mode
    
    
    def safely(self, act):
        if self.__safeSafelyMode:
            if not act[1]():
                print("WARNING:  ATTEMPED TO EXECUTE NON-ENABLED ACTION")
                return False
        try:
            act[2]()
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            self.__failure = sys.exc_info()
            return False
        finally:
            if len(act) > 3:
                self.annotate(act[3])
        return True
    
    
    def failure(self):
        return self.__failure
    
    
    def warning(self):
        return self.__warning
    
    
    def allEnabled(self, test):
        for a in test:
            name = a[0]
            guard = a[1]
            act = a[2]
            if not guard():
                return False
            self.safely((name, guard, act))
        return True
    
    
    def replay(
            self,
            test,
            catchUncaught=False,
            extend=False,
            checkProp=False,
            verbose=False,
            stopFail=True,
            returnCov=False,
            delay=None):
        '''
        Replays a test, either resetting first or extending current test
        (default is to restart).  Can either stop or keep going on
        failure, catch and notify about uncaught exceptions or throw them,
        and check or not check properties.  The returnCov setting adds a
        sequential record of coverage by step as another element of a
        return tuple.
        '''
        if not extend:
            self.restart()
        if returnCov:
            allS = set([])
            allB = set([])
            cov = []
        for a in test:
            name = a[0]
            if name == "<<RESTART>>":
                self.restart()
            guard = a[1]
            act = a[2]
            if verbose:
                print(name)
            if guard():
                if verbose:
                    print("EXECUTING")
                try:
                    act()
                except KeyboardInterrupt as e:
                    raise e
                except Exception as e:
                    self.__failure = sys.exc_info()
                    if catchUncaught:
                        if stopFail:
                            return False
                    else:
                        raise e
                if checkProp:
                    if (not self.check()) and stopFail:
                        return False
                if delay is not None:
                    time.sleep(delay)
            if returnCov:
                s = set(self.currStatements())
                b = set(self.currBranches())
                newS = s - allS
                newB = b - allB
                if (len(newS) > 0) or (len(newB) > 0):
                    cov.append((newS, newB))
                allS.update(s)
                allB.update(b)
        if returnCov:
            return (self.__failure is None, cov)
        return (self.__failure is None)
    
    
    def replayUntil(
            self,
            test,
            pred,
            catchUncaught=False,
            checkProp=False,
            stopFail=True):
        self.restart()
        newt = []
        if pred():
            return newt
    
        for a in test:
            name = a[0]
            guard = a[1]
            act = a[2]
    
            newt.append((name, guard, act))
            if guard():
                if catchUncaught:
                    try:
                        act()
                    except KeyboardInterrupt as e:
                        raise e
                    except BaseException:
                        self.__failure = sys.exc_info()
                        if stopFail:
                            return False
                        pass
                else:
                    act()
            if pred():
                return newt
            if checkProp:
                if not self.check():
                    return False
        return None
    
    
    def eqFail(self, f1, f2):
        if (f1[0] != f2[0]) or (repr(f1[1]) != repr(f2[1])):
            return False
        if f1[0] != AssertionError:
            return True
        # For assertions, require equal line nos.
        return ((f1[2].tb_lineno == f2[2].tb_lineno) and
                ((f1[2].tb_frame.f_code.co_filename) == (f2[2].tb_frame.f_code.co_filename)))
    
    
    def failsCheck(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, catchUncaught=True,
                            checkProp=True, verbose=verbose)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            if (failure is None) or self.eqFail(self.__failure, failure):
                return True
            else:
                return False
        if r is True:
            return False
        if (failure is None) or self.eqFail(self.__failure, failure):
            return True
        else:
            return False
    
    
    def fails(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, verbose=verbose, catchUncaught=True)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            if verbose:
                print("Got exception during replay!")
            if failure is None:
                return True
            if (self.__failure is not None) and self.eqFail(self.__failure, failure):
                return True
            else:
                return False
        if r is True:
            return False
        if (failure is None) or self.eqFail(self.__failure, failure):
            return True
        else:
            return False
    
    
    def failsAny(self, test, verbose=False, failure=None):
        try:
            r = self.replay(test, checkProp=True,
                            verbose=verbose, catchUncaught=True)
        except KeyboardInterrupt as e:
            raise e
        except BaseException:
            self.__failure = sys.exc_info()
            if (failure is None) or ((self.__failure[0] == failure[0]) and (
                    repr(self.__failure[1]) == repr(failure[1]))):
                return True
            return False
        if r is False:
            # self.__failure = sys.exc_info()
            if (failure is None) or ((self.__failure[0] == failure[0]) and (
                    repr(self.__failure[1]) == repr(failure[1]))):
                return True
            return False
        return False
    
    
    def P(self, t, pred, samples=10):
        success = 0.0
        for i in range(0, samples):
            if pred(t):
                success += 1.0
        return (success / samples)
    
    
    def forceP(self, t, pred, P=0.5, samples=10, replications=1):
        while (replications > 0):
            success = 0.0
            for i in range(0, samples):
                if pred(t):
                    success += 1.0
            replications -= 1
            if replications == 0:
                return (success / samples) >= P
            elif (success / samples) < P:
                return False
    
    
    def findProcessNondeterminism(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            delay=None,
            tries=1):
        for j in range(0, tries):
            try:
                self.saveTest(t, ".tmp.test")
                cmd = ["tstl_replay", ".tmp.test", "--hideOpaque", "--verbose"]
                if delay is not None:
                    cmd.extend(["--delay", str(delay)])
                out1 = subprocess.check_output(cmd, universal_newlines=True)
                out2 = subprocess.check_output(cmd, universal_newlines=True)
            finally:
                os.remove(".tmp.test")
            out1l = out1.split("\n")
            out2l = out2.split("\n")
            if ignoreExceptions:
                removeExceptions = (lambda l: "RAISED".find(l) != 0)
                out1l = list(filter(removeExceptions, out1l))
                out2l = list(filter(removeExceptions, out2l))
            if (out1l != out2l):
                action = -1
                for i in range(0, min(len(out1l), len(out2l))):
                    if out1l[i].find("STEP") == 0:
                        action = int(out1l[i].split(":")[0].split("#")[1]) + 1
                    if out1l[i] != out2l[i]:
                        if verbose:
                            print("=" * 50)
                            print("DIFFERENCE FOUND AT STEP", action)
                            print(out1l[i])
                            print("  VS.")
                            print(out2l[i])
                            print("=" * 50)
                        break
                return action
            else:
                if verbose:
                    print("NO DIFFERENCES IN OUTPUT FILES")
        return -1
    
    
    def iterateFindProcessNondeterminism(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            double=False,
            delay=None,
            tries=1):
        i = 1
        if verbose:
            print("TRYING WITH LENGTH:", i)
        p = self.findProcessNondeterminism(
            t[:i], ignoreExceptions, verbose, delay, tries)
        while (p == -1) and (i < len(t)):
            if not double:
                i += 1
            else:
                i *= 2
                if (i > len(t)):
                    i = len(t)
            if verbose:
                print("TRYING WITH LENGTH:", i)
            p = self.findProcessNondeterminism(
                t[:i], ignoreExceptions, verbose, delay, tries)
        return p
    
    
    def processNondeterministic(
            self,
            t,
            ignoreExceptions=True,
            verbose=False,
            iterate=False,
            double=True,
            delay=None,
            tries=1):
        for i in range(0, tries):
            if not iterate:
                nd = (self.findProcessNondeterminism(
                    t, ignoreExceptions, verbose, delay) != -1)
            else:
                nd = (self.iterateFindProcessNondeterminism(
                    t, ignoreExceptions, verbose, double, delay) != -1)
            if nd:
                return True
        return False
    
    
    def trajectoryItem(self, pools=None):
        ss = self.shallowState()
        o = set(self.opaque())
        if pools is not None:
            for p in self.pools():
                if p not in pools:
                    o.add(p)
        ti = {}
        for (name, vals) in ss:
            if name in o:
                continue
            if name.replace(
                "_REF",
                    "") in o:  # Assume if pool is opaque, so is reference
                continue
            ti[name] = {}
            for v in vals:
                try:
                    ti[name][v] = copy.deepcopy(vals[v])
                except BaseException:
                    ti[name][v] = "UNABLE TO COPY"
        return ti
    
    
    def stepNondeterministic(
            self,
            t,
            delay=1.0,
            delay0=None,
            tries=1,
            verbose=False,
            reportEqualFail=False,
            pools=None):
        """
        Checks if a test behaves nondeterministically (in terms of all
        non-opaque pool values produced) under an optional timing change.
        Default is to run with no delay for an initial capture of state,
        then run with a 1 second delay, and only run once.
        """
        trajectory = []
        self.restart()
        for s in t:
            self.safely(s)
            trajectory.append(self.trajectoryItem(pools))
            if delay0 is not None:
                time.sleep(delay0)
        for i in range(0, tries):
            pos = 0
            self.restart()
            for s in t:
                self.safely(s)
                try:
                    if (self.trajectoryItem(pools)) != (trajectory[pos]):
                        return True
                except BaseException:
                    if reportEqualFail:
                        raise
                if delay is not None:
                    time.sleep(delay)
                pos += 1
        return False
    
    
    def nondeterministic(
            self,
            t,
            delay=1.0,
            delay0=None,
            tries=1,
            reportEqualFail=False,
            pools=None):
        """
        Checks if a test behaves nondeterministically (in terms of final non-opaque pool values)
        under an optional timing change.  Default is to run with no delay for an initial capture
        of state, then run with a 1 second delay, and only run once.
        """
        self.replay(t, delay=delay0)
        ss = self.shallowState()
        o = set(self.opaque())
        if pools is not None:
            for p in self.pools():
                if p not in pools:
                    o.add(p)
        s0 = {}
        for (name, vals) in ss:
            if name in o:
                continue
            if name.replace(
                "_REF",
                    "") in o:  # Assume if pool is opaque, so is reference
                continue
            s0[name] = {}
            for v in vals:
                try:
                    s0[name][v] = copy.deepcopy(vals[v])
                except BaseException:
                    s0[name][v] = "UNABLE TO COPY"
        for i in range(0, tries):
            self.replay(t, delay=delay)
            ss = self.shallowState()
            s1 = {}
            for (name, vals) in ss:
                if name in o:
                    continue
                if name.replace(
                        "_REF", "") in o:  # Assume if pool is opaque, so is reference
                    continue
                s1[name] = {}
                for v in vals:
                    try:
                        s1[name][v] = copy.deepcopy(vals[v])
                    except BaseException:
                        s1[name][v] = "UNABLE TO COPY"
            try:
                if s0 != s1:
                    return True
            except BaseException:
                if reportEqualFail:
                    raise
        return False
    
    
    def verbose(self, bool):
        self.__verboseActions = bool
    
    
    def verboseOpaque(self, bool):
        self.__verbosePrintOpaque = bool
    
    
    def logOff(self):
        self.__log = None
    
    
    def logAll(self):
        self.__log = 'All'
    
    
    def setLog(self, level):
        self.__log = level
    
    
    def setLogAction(self, f):
        self.__logAction = f
    
    
    def logPrint(self, name, code, text, after):
        print("[", end=' ')
        if after:
            print("POST", end=' ')
        print("LOG " + name + "  :  " + str(code) + "] " + str(text))
    
    
    def testCandidates(self, t, n):
        # Fix so that if n means removal is single items, you just return all the
        # relevant removals
        candidates = []
        if t == []:
            return [[]]
        s = int(len(t) / n)
        if (s == 1):
            n = len(t)
        for i in range(0, n):
            tc = t[0:i * s]
            tc.extend(t[(i + 1) * s:])
            candidates.append(tc)
        return candidates
    
    
    def reduce(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=True,
            rgen=None,
            amplify=False,
            amplifyReplications=1,
            stopFound=False,
            tryFast=True,
            testHandler=None,
            findLocations=False,
            noResetSplit=False,
            safeReduce=False,
            saveIntermediate=None):
        """
        This function takes a test that has failed, and attempts to reduce
        it using a simplified version of Zeller's Delta-Debugging
        algorithm.  pruneGuards determines if disabled guards are
        automatically removed from reduced tests, keepLast determines if
        the last action must remain unchanged (this is useful for keeping
        the fault detected from changing).
    
        amplify changes behavior from "preserve (or find) pred(test) =
        True" to "increase the value of pred(test)"
    
        tryFast means that instead of the binary search, reduce assumes
        the test is already close to 1-minimal (e.g., from normalization)
        and skips right to the smallest granularity, searching for a
        close-by 1-minimal test.
    
        testHandler is an optional function to pass in.  It can do things
        like check for new coverage from a candidate run, and collect such
        tests for quick testing or GA-based exploration.
        """
        try:
            test_before_reduce(self)
        except BaseException:
            pass
    
        intermediate = 0
    
        if len(test) < 2:
            return test
    
        if amplify:
            currBest = pred(test)
            if verbose:
                print("Starting best value:", currBest)
    
        if findLocations:
            ntest = []
            i = 0
            for a in test:
                name = a[0]
                guard = a[1]
                act = a[2]
                ntest.append((name, guard, act, i))
                i += 1
            test = ntest
    
        if keepLast:
            tb = test[:-1]
            addLast = [test[-1]]
        else:
            tb = test
            addLast = []
    
        n = 2
    
        if tryFast:
            n = len(tb)
    
        lastRemove = 0
    
        count = 0
        stests = {}
        while True:
            # If there is nothing left in the test, either the null test fails,
            # of you just need to return the keepLast item
            if len(tb) == 0:
                return tb + addLast
            if verbose or safeReduce:
                # We only perform a sanity check to avoid infinite loops if verbose
                # or if safeReduce is True
                stest = self.captureReplay(tb)
                assert ((stest, n, lastRemove) not in stests)
                stests[(stest, n, lastRemove)] = True
            count += 1
            c = self.testCandidates(tb, n)
            if lastRemove > 0:
                c = c[lastRemove:] + c[:lastRemove]
            if rgen:
                rgen.shuffle(c)
            reduced = False
            removePos = -1
            truePos = -1
            for tc in c:
                removePos += 1
                if verbose == "VERY":
                    print("Trying candidate of length", len(tc + addLast))
                if not findLocations:
                    v = pred(tc + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in tc + addLast])
                if testHandler is not None:
                    testHandler()
                if amplify:
                    if v > currBest:
                        for rep in range(0, amplifyReplications - 1):
                            if not findLocations:
                                v = pred(tc + addLast)
                            else:
                                v = pred([(x[0], x[1], x[2])
                                          for x in tc + addLast])
                            if v <= currBest:
                                break
                        if v > currBest:
                            currBest = v
                            v = True
                            if verbose:
                                print("New best value:", currBest)
                        else:
                            v = False
                    else:
                        v = False
                if v:
                    if stopFound:
                        return (tc + addLast)
                    if verbose == "SHOW":
                        print("REMOVED:")
                        self.prettyPrintRemoved(tb, tc)
                    tb = tc
                    if not noResetSplit:
                        n = 2
                    else:
                        if n > len(tb):
                            n = len(tb)
                    if verbose:
                        print("Reduced test length to", len(tb + addLast))
                    if pruneGuards:
                        self.restart()
                        newtb = []
                        for a in tb:
                            if a[0] == "<<RESTART>>":
                                newtb.append(a)
                                self.restart()
                            elif a[1]():
                                newtb.append(a)
                                try:
                                    a[2]()
                                except KeyboardInterrupt as e:
                                    raise e
                                except BaseException:
                                    pass
                        if verbose:
                            if len(newtb) < len(tb):
                                print("Guard pruning reduced test length to",
                                      len(newtb + addLast))
                                if verbose == "SHOW":
                                    print("REMOVED:")
                                    self.prettyPrintRemoved(tb, newtb)
                        tb = newtb
                    if tryFast:
                        n = len(tb)
                        truePos = (lastRemove + removePos) % max(len(tb), 1)
                        lastRemove = truePos
                        if verbose == "VERY":
                            print("check #", truePos, removePos, lastRemove)
                    if saveIntermediate is not None:
                        self.saveTest(
                            tb +
                            addLast,
                            saveIntermediate +
                            "." +
                            str(intermediate) +
                            ".test")
                        intermediate += 1
                    reduced = True
                    break
            if not reduced:
                if (n == len(tb)):
                    try:
                        test_after_reduce(self)
                    except BaseException:
                        pass
                    return tb + addLast
                n = min(n * 2, len(tb))
                if verbose:
                    print("Failed to reduce, increasing granularity to", n)
            elif False and (not reduced) and tryFast and (lastRemove != 0):
                if verbose:
                    print(
                        "Trying a pass from the beginning, was at position",
                        lastRemove)
                lastRemove = 0
                n = len(tb)
            elif len(tb) == 1:
                try:
                    test_after_reduce(self)
                except BaseException:
                    pass
    
                if not findLocations:
                    v = pred([] + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in [] + addLast])
                if amplify:
                    if v > currBest:
                        v = True
                    else:
                        v = False
                if v:
                    return ([] + addLast)
    
                if not findLocations:
                    v = pred(tc + addLast)
                else:
                    v = pred([(x[0], x[1], x[2]) for x in tc + addLast])
                if amplify:
                    if v > currBest:
                        v = True
                    else:
                        v = False
                if v:
                    return (tc + addLast)
                else:
                    return (tb + addLast)
    
    
    def tryCompose(
            tests,
            pred,
            pruneGuards=False,
            keepLast=False,
            verbose=True,
            rgen=None,
            amplify=False,
            combs=1):
        newt = []
        for t in tests:
            newt.extend(t)
        newt = newt * combs
        return reduce(newt, pred, pruneGuards, keepLast, verbose, rgen, amplify)
    
    
    def reductions(
            self,
            test,
            pred,
            pruneGuards=True,
            tryFast=True,
            keepLast=False,
            verbose=True,
            recursive=1,
            useClasses=True,
            limit=None):
        # use recursive = -1 for infinite recursion (all tests)
        r = self.reduce(test, pred, pruneGuards=pruneGuards,
                        keepLast=keepLast, verbose=verbose, tryFast=tryFast)
        reductions = [r]
        anyNew = True
        filterActs = set()
        impossibleSets = []
        analyzedCount = 0
        analyzed = []
        while anyNew:
            recursive = recursive - 1
            filterActs = set([])
            for r in reductions:
                for s in r:
                    if not set([s]) in impossibleSets:
                        filterActs.add(s)
    
            anyNew = False
            sys.stdout.flush()
            for i in range(1, len(filterActs)):
                ncombos = 0
                if verbose:
                    print("ANALYZING SIZE", i, "COMBINATIONS")
                combs = combinations(filterActs, i)
                for c in combs:
                    analyzedCount += 1
                    # if (analyzedCount % 10) == 0:
                    #    print "ANALYZED:",analyzedCount
                    if (limit is not None) and (analyzedCount > limit):
                        print("REDUCTION LIMIT EXCEEDED")
                        return reductions
                    cs = set(c)
                    if cs in analyzed:
                        continue
                    analyzed.append(cs)
                    skipCombo = False
                    for iset in impossibleSets:
                        if [x for x in iset if x not in cs] == []:
                            skipCombo = True
                            break
                    if skipCombo:
                        continue
                    skipCombo = False
                    for r in reductions:
                        if [x for x in r if x in cs] == []:
                            skipCombo = True
                            break
                    if skipCombo:
                        continue
                    ncombos += 1
                    ac = list(map(self.actionClass, cs))
                    if useClasses:
                        tfilter1 = [
                            x for x in test if self.actionClass(x) not in ac]
                        pfilter1 = pred(tfilter1)
                    else:
                        pfilter1 = False
                    tfilter2 = [x for x in test if x not in cs]
                    pfilter2 = pred(tfilter2)
                    if pfilter1:
                        rfilter1 = self.reduce(
                            tfilter1,
                            pred,
                            pruneGuards=pruneGuards,
                            keepLast=keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if rfilter1 not in reductions:
                            if recursive != 0:
                                anyNew = True
                            if verbose:
                                print("ADDING NEW TEST OF LENGTH", len(rfilter1))
                            reductions.append(rfilter1)
                    if pfilter2:
                        rfilter2 = self.reduce(
                            tfilter2,
                            pred,
                            pruneGuards=pruneGuards,
                            keepLast=keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if rfilter2 not in reductions:
                            if recursive != 0:
                                anyNew = True
                            if verbose:
                                print("ADDING NEW TEST OF LENGTH", len(rfilter2))
                            reductions.append(rfilter2)
                    if (not pfilter1) and (not pfilter2):
                        if cs not in impossibleSets:
                            if verbose:
                                print("FOUND IMPOSSIBLE RESTRICTION:", [
                                      self.prettyName(x[0]) for x in cs])
                            impossibleSets.append(cs)
                if verbose:
                    print("ANALYZED", ncombos, "COMBINATIONS")
    
        return reductions
    
    
    def poolUses(self, str):
        uses = []
        for p in self.__pools:
            pos = str.find(p, 0)
            while pos != -1:
                access = str[pos:str.find("]", pos) + 1]
                if access not in uses:
                    uses.append(
                        (access, access[access.find("[") + 1:access.find("]")]))
                pos = str.find(p, pos + 1)
        return uses
    
    
    def powerset(self, iterable):
        xs = list(iterable)
        return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))
    
    
    def reduceEssentials(
            self,
            test,
            original,
            pred,
            pruneGuards=True,
            keepLast=False,
            tryFast=True):
        possibleRemove = test
        if keepLast:
            possibleRemove = test[:-1]
        removals = list(self.powerset(possibleRemove))
        removals = sorted(removals, key=lambda x: len(x), reverse=True)
        workingRemovals = []
        failedRemovals = []
        for rset in removals:
            if rset == []:
                continue
            foundSuperset = False
            for (w, _) in workingRemovals:
                allPresent = True
                for r in rset:
                    if r not in w:
                        allPresent = False
                        break
                if allPresent:
                    foundSuperset = True
                    break
            if foundSuperset:
                continue
            newOrig = [x for x in original if x not in rset]
            if pred(newOrig):
                reduced = self.reduce(
                    newOrig, pred, pruneGuards, keepLast, tryFast=tryFast)
                workingRemovals.append((rset, reduced))
            else:
                failedRemovals.append(rset)
        return (workingRemovals, failedRemovals)
    
    
    def actionReplace(self, action, old, new):
        if action[0] == old:
            return self.__names[new]
        else:
            return action
    
    
    def actionModify(self, action, old, new):
        name = action[0]
        newName = name.replace(old, new)
        return self.__names[newName]
    
    
    def levDist(self, s1, s2):
        if len(s1) > len(s2):
            s1, s2 = s2, s1
        distances = list(range(len(s1) + 1))
        for index2, char2 in enumerate(s2):
            newDistances = [index2 + 1]
            for index1, char1 in enumerate(s1):
                if char1 == char2:
                    newDistances.append(distances[index1])
                else:
                    newDistances.append(1 + min((distances[index1],
                                                 distances[index1 + 1],
                                                 newDistances[-1])))
            distances = newDistances
        return distances[-1]
    
    
    def getEnabled(self, test, checkEnabled):
        self.restart()
        enableChange = {}
        for i in range(0, len(test)):
            if checkEnabled:
                enableChange[i] = [x[0] for x in self.enabled()]
                self.safely(test[i])
            else:
                enableChange[i] = [x[0] for x in self.actions()]
        for i in range(0, len(test)):
            enableChange[i] = sorted(
                enableChange[i], key=lambda x: self.__orderings[x])
        return enableChange
    
    
    def numReassigns(self, test):
    
        if not self.__noReassigns:
            return 0
    
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i, p))
                        else:
                            lhsPools.append(p)
            i += 1
        return len(reuses)
    
    
    def reduceLengthStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None,
            tryFast=True):
        if verbose == "VERY":
            print("STARTING REDUCE LENGTH STEP")
        # Replace any action with another action, if that allows test to be
        # further reduced
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        stop = len(test)
        if keepLast:
            stop -= 1
    
        for i in range(0, stop):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if name1 != name2:
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i + 1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        rtestC = self.reduce(
                            testC,
                            pred,
                            pruneGuards,
                            keepLast,
                            verbose=verbose,
                            tryFast=tryFast)
                        if len(rtestC) < len(test):
                            if verbose:
                                print(
                                    "NORMALIZER: RULE ReduceAction: STEP",
                                    i,
                                    name1,
                                    "-->",
                                    name2,
                                    "REDUCING LENGTH FROM",
                                    len(test),
                                    "TO",
                                    len(rtestC))
                            return (True, rtestC)
        return (False, test)
    
    
    def replaceAllStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE ALL STEP")
        # Replace all occurrences of an action with a simpler action
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        donePairs = []
        for i in range(0, len(test)):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if (self.__orderings[name1] > self.__orderings[name2]) and (
                        (name1, name2) not in donePairs):
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    donePairs.append((name1, name2))
                    testC = [self.actionReplace(x, name1, name2) for x in test]
                    if keepLast:
                        testC = testC[:-1] + [test[-1]]
                        if testC == test:
                            continue
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SimplifyAll:",
                                  name1, "-->", name2)
                        return (True, testC)
        return (False, test)
    
    
    def replacePoolStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE POOL STEP")
        # Replace pools with lower-numbered pools
    
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)
    
        # First try the simple version:
    
        if self.__noReassigns:
    
            for (p, i) in pools:
                for n in range(0, int(i)):
                    new = p.replace("[" + i + "]", "[" + str(n) + "]")
                    testC = [self.actionModify(x, p, new) for x in test]
                    if (testC != test) and (self.numReassigns(
                            testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE ReplacePool:", p, "WITH", new)
                        return (True, testC)
    
            # Remained of this code is now not needed, probably, due to
            # noReassignRule
            return (False, test)
    
        # Reduce number of pools but may need to move assignment to a later
        # position, or only change after the position
        for pos in range(0, len(test)):
            for (p, i) in pools:
                for n in range(0, int(i)):
                    new = p.replace("[" + i + "]", "[" + str(n) + "]")
                    prefix = []
                    moved = []
                    for j in range(0, pos):
                        if new in test[j][0]:
                            moved.append(test[j])
                        else:
                            prefix.append(test[j])
                    suffix = [self.actionModify(x, p, new)
                              for x in moved + test[pos:]]
                    newPrefix = [self.actionModify(x, p, new) for x in prefix]
                    newSuffix = [self.actionModify(x, p, new) for x in suffix]
                    testC = newPrefix + newSuffix
                    if (testC != test) and (self.numReassigns(
                            testC) <= reassignCount) and pred(testC):
                        if verbose:
                            if pos == 0:
                                print(
                                    "NORMALIZER: RULE ReplacePool:", p, "WITH", new)
                            else:
                                print("NORMALIZER: RULE ReplaceMovePool:",
                                      p, "WITH", new, " -- MOVED TO", pos)
                        return (True, testC)
                    # Not possible, try with only replacing between pos and pos2
                    for pos2 in range(len(test), pos, -1):
                        prefix = test[:pos]
                        suffix = [self.actionModify(x, p, new)
                                  for x in test[pos:pos2]]
                        testC = prefix + suffix + test[pos2:]
                        if (testC != test) and (self.numReassigns(
                                testC) <= reassignCount) and pred(testC):
                            if verbose:
                                print("NORMALIZER: RULE ReplacePool:", p,
                                      "WITH", new, "FROM", pos, "TO", pos2)
                            return (True, testC)
        return (False, test)
    
    
    def replaceSingleStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING REPLACE SINGLE STEP")
        # Replace any single action with a lower-numbered action
        enableChange = self.getEnabled(test, checkEnabled)
    
        reassignCount = self.numReassigns(test)
    
        stop = len(test)
        if keepLast:
            stop -= 1
    
        for i in range(0, stop):
            name1 = test[i][0]
            if i not in enableChange:
                continue
            for name2 in enableChange[i]:
                if self.__orderings[name1] > self.__orderings[name2]:
                    if (distLimit is not None) and (
                            self.levDist(name1, name2) > distLimit):
                        continue
                    testC = test[0:i] + [self.__names[name2]] + test[i + 1:]
                    if (self.numReassigns(testC) <= reassignCount) and pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SimplifySingle: STEP",
                                  i, name1, "-->", name2)
                        return (True, testC)
        return (False, test)
    
    
    def swapPoolStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING SWAP POOL STEP")
        # Swap two pool uses in between two positions, if this lowers the minimal
        # action ordering between them
        pools = []
        for s in test:
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p)
    
        reassignCount = self.numReassigns(test)
    
        swaps = []
        for (p1, i1) in pools:
            for (p2, i2) in pools:
                for pos1 in range(0, len(test)):
                    for pos2 in range(len(test), pos1, -1):
                        if (p1 != p2) and (p1.split("[")[0] == p2.split("[")[0]):
                            p1new = p1.replace("[" + i1 + "]", "[" + i2 + "]")
                            p2new = p2.replace("[" + i2 + "]", "[" + i1 + "]")
                            p2newTemp = p2.replace("[" + i2 + "]", "[**]")
                            tempTest = [(x[0].replace(p2, p2newTemp), x[1], x[2])
                                        for x in test[pos1:pos2]]
                            tempTest2 = [(x[0].replace(p1, p1new), x[1], x[2])
                                         for x in tempTest]
                            testC = test[:pos1] + [self.actionModify(
                                x, p2newTemp, p2new) for x in tempTest2] + test[pos2:]
                            leastTestC = -1
                            leastTest = -1
                            for s in range(0, len(test)):
                                if test[s] != testC[s]:
                                    ordTest = self.__orderings[test[s][0]]
                                    if (leastTest == -1) or (ordTest < leastTest):
                                        leastTest = ordTest
                                    ordTestC = self.__orderings[testC[s][0]]
                                    if (leastTestC == -1) or (ordTestC < leastTestC):
                                        leastTestC = ordTestC
                            if leastTestC < leastTest:
                                if (self.numReassigns(testC) <=
                                        reassignCount) and pred(testC):
                                    if verbose:
                                        print(
                                            "NORMALIZER: RULE SwapPool:",
                                            p1,
                                            "AND",
                                            p2,
                                            "BETWEEN STEP",
                                            pos1,
                                            "AND",
                                            pos2)
                                    return (True, testC)
        return (False, test)
    
    
    def opaque(self):
        return self.__opaque
    
    
    def uniqueVals(self):
        ss = self.shallowState()
        uvals = []
        for (pool, vals) in ss:
            if pool not in self.__opaque:
                for v in list(vals.values()):
                    if v is not None:
                        if (pool, str(v)) not in uvals:
                            uvals.append((pool, str(v)))
        return uvals
    
    
    def coversUnique(self, val, catchUncaught=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            uv = self.uniqueVals()
            return val in uv
        return coverPred
    
    
    def noReassignStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if not self.__noReassigns:
            return (False, test)
    
        if verbose == "VERY":
            print("STARTING NOREASSIGNS STEP")
        # Replace reassignments with fresh variables
        pools = []
        lhsPools = []
        reuses = []
    
        i = 0
        for s in test:
            if " = " in s[0]:
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if len(lhsp) == 1:
                    for p in self.poolUses(lhs):
                        if p in lhsPools:
                            reuses.append((i, p))
                        else:
                            lhsPools.append(p)
            for p in self.poolUses(s[0]):
                if p not in pools:
                    pools.append(p[0])
            i += 1
    
        for (i, pu) in reuses:
            prefix = test[0:i]
            (p, pnum) = pu
            newp = None
            for ni in range(0, self.__psize[p.split(
                    "[")[0].replace(self.__poolPrefix, "")]):
                if int(ni) == int(pnum):
                    continue
                tnewp = p.replace("[" + str(pnum) + "]", "[" + str(ni) + "]")
                print("REPLACING", tnewp, ni, p, pnum)
                if tnewp not in pools:
                    newp = tnewp
                    break
            if newp is None:
                continue
            if verbose:
                print("NORMALIZER: RULE NoReassigns:",
                      i, test[i][0], p, "TO", newp)
            suffix = []
            for s in test[i:]:
                suffix.append(self.actionModify(s, p, newp))
            return (True, prefix + suffix)
    
        return (False, test)
    
    
    def swapActionOrderStep(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None):
        if verbose == "VERY":
            print("STARTING SWAP ACTION ORDER STEP")
        # Try to swap any out-of-order actions
        lastMover = len(test)
        if keepLast:
            lastMover -= 1
    
        for i in range(0, lastMover):
            for j in range(i + 1, lastMover):
                step1 = test[i][0]
                step2 = test[j][0]
                if self.__orderings[step2] < self.__orderings[step1]:
                    frag1 = test[:i]
                    frag2 = [test[j]]
                    frag3 = test[i + 1:j]
                    frag4 = [test[i]]
                    frag5 = test[j + 1:]
                    testC = frag1 + frag2 + frag3 + frag4 + frag5
                    if pred(testC):
                        if verbose:
                            print("NORMALIZER: RULE SwapAction:", i,
                                  test[i][0], "WITH STEP", j, test[j][0])
                        return (True, testC)
        return (False, test)
    
    
    def clearNormalizationCache(self):
        self.__simplifyCache = {}
    
    
    def swapPools(self, test, p1, p2, after=0):
        poolsByLength = sorted(self.__pools, key=len, reverse=True)
        tPrefix = test[:after]
        test = test[after:]
        p1new = self.__poolPrefix + p1
        p2new = self.__poolPrefix + p2
        for p in poolsByLength:
            if p in p1new:
                p1new = p + "[" + p1new.split(p)[1] + "]"
        for p in poolsByLength:
            if p in p2new:
                p2new = p + "[" + p2new.split(p)[1] + "]"
        newTest = [x[0].replace(p1new, "!!P1NEW!!") for x in test]
        newTest = [x.replace(p2new, p1new) for x in newTest]
        newTest = [x.replace("!!P1NEW!!", p2new) for x in newTest]
        newTest = [self.__names[x] for x in newTest]
        return tPrefix + newTest
    
    
    def alphaConvert(self, test, verbose=False):
        """
        This ONLY performs renaming of pools to lowest values possible; it
        CAN in theory cause worse normalization.
        """
        count = {}
        changed = True
        while changed:
            if verbose:
                print("RESTARTING")
            changed = False
            for p in self.__pools:
                count[p] = 0
            i = -1
            for s in test:
                i += 1
                if "=" not in s[0]:
                    continue
                lhs = s[0].split(" = ")[0]
                lhsp = self.poolUses(lhs)
                if verbose:
                    print("EXAMINING:", s[0], lhsp, count)
                for (p, n) in lhsp:
                    basep = p.split("[")[0]
                    if verbose:
                        print((p, n), "BASE", basep, count[basep])
                    if count[basep] < int(n):
                        p1new = p
                        p2new = p.replace(n, str(count[basep]))
                        if verbose:
                            print("REPLACING", p1new, "WITH", p2new)
                        newTest = [x[0].replace(p1new, "!!P1NEW!!") for x in test[i:]]
                        newTest = [x.replace(p2new, p1new) for x in newTest]
                        newTest = [x.replace("!!P1NEW!!", p2new) for x in newTest]
                        newTest = [self.__names[x] for x in newTest]
                        test = test[:i] + newTest
                        # self.prettyPrintTest(test)
                        count[basep] += 1
                        changed = True
                        break
                    elif int(n) >= count[basep]:
                        count[basep] += 1
                if changed:
                    break
        return test
    
    
    def normalize(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            speed="FAST",
            checkEnabled=False,
            distLimit=None,
            reorder=True,
            noReassigns=False,
            useCache=True,
            tryFast=True):
        """
        Attempts to produce a normalized test case
        """
        try:
            test_before_normalize(self)
        except BaseException:
            pass
    
        if noReassigns:
            self.__noReassigns = True
        else:
            self.__noReassigns = False
    
        # Check the cache
        stest = self.captureReplay(test)
        if useCache and (stest in self.__simplifyCache):
            if verbose:
                print("NORMALIZER: FOUND TEST IN CACHED RESULTS")
            return self.__simplifyCache[stest]
        history = [stest]
    
        # Turns off requirement that you can't initialize an unused variable,
        # allowing reducer to take care of redundant assignments
        # self.relax()
    
        # Default speed is fast, if speed not recognized
        simplifiers = [
            self.noReassignStep,
            self.replaceAllStep,
            self.replacePoolStep,
            self.replaceSingleStep,
            self.swapPoolStep,
            self.swapActionOrderStep,
            self.reduceLengthStep]
        # simplifiers = [self.noReassignStep, self.replaceAllStep, self.replaceSingleStep,
        #                self.swapActionOrderStep, self.reduceLengthStep]
        # Default approach tries a reduce after any change
        reduceOnChange = True
        if speed == "SLOW":
            simplifiers = [
                self.reduceLengthStep,
                self.replaceAllStep,
                self.replacePoolStep,
                self.replaceSingleStep,
                self.swapPoolStep,
                self.swapActionOrderStep]
        elif speed == "ONEREDUCE":
            # Runs one attempt at length reduction before normal simplification,
            # without reduction step
            (changed, test) = self.reduceLengthStep(test, pred, pruneGuards,
                                                    keepLast, verbose, checkEnabled,
                                                    distLimit, tryFast=tryFast)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
            simplifiers = [
                self.replaceAllStep,
                self.replacePoolStep,
                self.replaceSingleStep,
                self.swapPoolStep,
                self.swapActionOrderStep]
        elif speed == "MEDIUM":
            # Runs one attempt at length reduction before normal simplification
            (changed, test) = self.reduceLengthStep(test, pred,
                                                    pruneGuards, keepLast, verbose, tryFast=tryFast)
            if changed:
                stest = self.captureReplay(test)
                history.append(stest)
        elif speed == "VERYFAST":
            reduceOnChange = False
            if distLimit is None:
                distLimit = 3  # maximum of 3 char change when replacing actions!
                # allows numeric switches, simple pool modifications, but very few method changes
        elif speed == "VERYFASTREDUCE":
            reduceOnChange = True
            if distLimit is None:
                distLimit = 3  # maximum of 3 char change when replacing actions!
                # allows numeric switches, simple pool modifications, but very few method changes
    
        numChanges = 0
        changed = True
        stests = {}
        while changed:
            stest = self.captureReplay(test)
            assert (stest not in stests)
            stests[stest] = True
            changed = False
            if reorder:
                newSimplifiers = list(simplifiers)
            for s in simplifiers:
                oldTest = test
                (changed, test) = s(test, pred, pruneGuards,
                                    keepLast, verbose, checkEnabled, distLimit)
                if changed:
                    if reduceOnChange:
                        test = self.reduce(test, pred, pruneGuards,
                                           keepLast, verbose=verbose, tryFast=True)
                    if verbose:
                        self.prettyPrintTest(test)
                    stest = self.captureReplay(test)
                    if useCache and (stest in self.__simplifyCache):
                        if verbose:
                            print("NORMALIZER: FOUND TEST IN CACHED RESULTS")
                        result = self.__simplifyCache[stest]
                        for t in history:
                            self.__simplifyCache[t] = result
                        # self.stopRelax()
                        return result
                    history.append(stest)
                    if reorder:
                        simplifiers = newSimplifiers
                    break
                elif reorder:
                    newSimplifiers.remove(s)
                    newSimplifiers.append(s)
    
        # No changes, this is 1-simple (fix-point)
        try:
            test_after_normalize(self)
        except BaseException:
            pass
    
        # self.stopRelax()
        # restore normal TSTL semantics!
    
        # Update the simplification cache and return
        if useCache:
            for t in history:
                self.__simplifyCache[t] = test
        return test
    
    
    def freshSimpleVariants(self, name, previous, replacements):
        prevNames = [x[0] for x in previous]
        prevNames.reverse()
        lastAppear = []
        eqFind = name.find("=")
        if eqFind != -1:
            poolAssign = name[0:eqFind - 1]
        else:
            poolAssign = None
        pools = self.poolUses(name)
        lastAppearMap = {}
        for (p, i) in pools:
            for n in prevNames:
                if p[0:p.find("[")] in self.__consts:
                    if n.find(p + " = ") == -1:
                        continue
                lastAppearMap[p] = [n]
                break
            skeys = list(replacements.keys())
            skeys = [x for x in skeys if x < len(previous)]
            skeys = sorted(skeys, reverse=True)
            for i in skeys:
                foundAny = False
                for r in replacements[i]:
                    if p[0:p.find("[")] in self.__consts:
                        if r.find(p + " = ") == -1:
                            continue
                    foundAny = True
                    if p in lastAppearMap:
                        lastAppearMap[p].append(r)
                    else:
                        lastAppearMap[p] = [r]
                if foundAny:
                    break
        for n in lastAppearMap:
            lastAppear.extend(lastAppearMap[n])
    #    print "LAST APPEAR = ",lastAppear
        freshSimples = []
        for (p, i) in pools:
            if p == poolAssign:
                continue
            for n in self.__names:
                if n in lastAppear:
                    continue
                if (p + " = ") in n:
                    uses = self.poolUses(n[n.find("=") + 1:])
                    if uses == []:
                        freshSimples.append([self.__names[n], self.__names[name]])
        freshSimples = sorted(
            freshSimples, key=lambda x: self.__orderings[x[0][0]])
        return freshSimples
    
    
    def generalize(
            self,
            test,
            pred,
            pruneGuards=True,
            keepLast=False,
            verbose=False,
            checkEnabled=False,
            distLimit=None,
            returnCollect=False,
            collected=None,
            depth=0,
            silent=False,
            targets=None,
            fresh=True):
    
        if collected is None:
            collected = {}
    
        newCollected = {}
    
        # Change so double assignments are allowed
        # self.relax()
    
        enableChange = self.getEnabled(test, checkEnabled)
    
        canReplace = {}
        canSwap = {}
        canMakeSimple = {}
        for i in range(0, len(test)):
            canSwap[i] = []
        for i in range(0, len(test)):
            canReplace[i] = []
            canMakeSimple[i] = []
            if i not in enableChange:
                continue
            for a in enableChange[i]:
                if (distLimit is not None) and (
                        self.levDist(a, test[i][0]) > distLimit):
                    continue
                if a != test[i][0]:
                    testC = test[:i] + [self.__names[a]] + test[i + 1:]
                    if pred(testC):  # and self.allEnabled(testC):
                        if returnCollect:
                            stestC = self.captureReplay(testC)
                            if stestC not in collected:
                                collected[stestC] = True
                                newCollected[stestC] = True
                            if stestC in targets:
                                # self.stopRelax()
                                return (True, stestC, dict(collected))
                        canReplace[i].append(a)
            for j in range(i + 1, len(test)):
                if i == j or test[i][0] == test[j][0]:
                    continue
                testC = test[:i] + [test[j]] + \
                    test[i + 1:j] + [test[i]] + test[j + 1:]
                if pred(testC):  # and self.allEnabled(testC):
                    if returnCollect:
                        stestC = self.captureReplay(testC)
                        if stestC not in collected:
                            collected[stestC] = True
                            newCollected[stestC] = True
                            if stestC in targets:
                                # self.stopRelax()
                                return (True, stestC, dict(collected))
                    canSwap[i].append(j)
                    canSwap[j].append(i)
            if fresh:
                for v in self.freshSimpleVariants(
                        test[i][0], test[:i], canReplace):
                    testC = test[:i] + v + test[i + 1:]
                    # self.prettyPrintTest(testC)
                    if pred(testC) and self.allEnabled(testC):
                        canMakeSimple[i].append(v)
        if not silent:
            noOrder = []
            endSwappable = -1
            for i in range(0, len(test)):
                if endSwappable >= i:
                    continue
                foundSwap = False
                for j in range(len(test) - 1, i, -1):
                    allSwappable = True
                    for k1 in range(i, j + 1):
                        for k2 in range(k1 + 1, j + 1):
                            if k2 not in canSwap[k1]:
                                allSwappable = False
                                break
                        if not allSwappable:
                            break
                    if allSwappable:
                        noOrder.append((i, j))
                        for k1 in range(i, j + 1):
                            for k2 in range(i, j + 1):
                                if k2 in canSwap[k1]:
                                    canSwap[k1].remove(k2)
                        endSwappable = j
                        break
            for i in range(0, len(test)):
                for (begin, end) in noOrder:
                    if i == begin:
                        print("#[")
                pn = self.prettyName(test[i][0])
                spaces = " " * (90 - len(pn) - len(" # STEP"))
                print(self.prettyName(test[i][0]), spaces, "# STEP", i)
                if canReplace[i] != []:
                    firstRep = None
                    lastRep = None
                    for rep in canReplace[i]:
                        if firstRep is None:
                            firstRep = rep
                            lastRep = rep
                        elif self.__orderings[rep] != (self.__orderings[lastRep] + 1):
                            if firstRep == lastRep:
                                print("#  or", self.prettyName(firstRep))
                            else:
                                print("#  or", self.prettyName(firstRep))
                                print("#   -", self.prettyName(lastRep))
                            firstRep = rep
                            lastRep = rep
                        else:
                            lastRep = rep
                    if firstRep == lastRep:
                        print("#  or", self.prettyName(firstRep))
                    else:
                        print("#  or", self.prettyName(firstRep))
                        print("#   -", self.prettyName(lastRep))
                if canMakeSimple[i] != []:
                    for v in canMakeSimple[i]:
                        print("#  or (")
                        for s in v[:-1]:
                            print("#     ", self.prettyName(s[0]), ";")
                        print("#     ", self.prettyName(v[-1][0]))
                        print("#     )")
                if canSwap[i] != []:
                    if len(canSwap[i]) == 1:
                        print("#  swaps with step", end=' ')
                    else:
                        print("#  swaps with steps", end=' ')
                    for j in canSwap[i]:
                        print(j, end=' ')
                    print()
                for (begin, end) in noOrder:
                    if i == end:
                        print("#] (steps in [] can be in any order)")
        # Restore semantics
        # self.stopRelax()
        if returnCollect:
            if depth == 0:
                return (False, None, dict(collected))
            else:
                allCollected = dict(collected)
                for c in newCollected:
                    (found,
                     stest,
                     cGen) = self.generalize(self.replayable(c),
                                             pred,
                                             pruneGuards,
                                             keepLast,
                                             verbose,
                                             checkEnabled,
                                             distLimit,
                                             returnCollect=True,
                                             collected=allCollected,
                                             depth=depth - 1,
                                             silent=True,
                                             targets=targets)
                    for c2 in cGen:
                        if c2 not in allCollected:
                            allCollected[c2] = True
                    if found is True:
                        return (True, stest, dict(allCollected))
                return (False, None, dict(allCollected))
    
    
    def relax(self):
        self.__relaxUsedRestriction = True
    
    
    def setReload(self, val):
        self.__doReload = val
    
    
    def stopRelax(self):
        self.__relaxUsedRestriction = False
    
    
    def moduleLocations(self):
        # This code may not be completely robust, but it seems to work, unless
        # previous approaches
        locs = []
        for m in self.__importModules:
            try:
                p = m.__path__
                if p != []:
                    locs.extend(m.__path__)
                else:
                    raise AttributeError
            except AttributeError:
                try:
                    f = m.__file__
                    if ("lib-dynload" in f) or ("site-packages" not in f):
                        continue  # skip system code
                    locs.append(m.__name__)
                except AttributeError:
                    pass
        return locs
    def __updateCov(self, extendCov=False):
        if not extendCov:
            self.__newBranches = set()
            self.__newStatements = set()
        newCov = self.__cov.get_data()
        if self.__oldCovData is None:
            self.__oldCovData = coverage.CoverageData()
        self.__oldCovData.update(newCov)
        if newCov.measured_files() is None:
            return
        for src_file in newCov.measured_files():
            thisArcs = newCov.arcs(src_file)
            if thisArcs is None:
                continue  # assume if we have arcs we have lines
            for arc in thisArcs:
                branch = (src_file, arc)
                if branch not in self.__allBranches:
                    self.__allBranches.add(branch)
                    self.__newBranches.add(branch)
                    self.__newCurrBranches.add(branch)
                if branch not in self.__currBranches:
                    self.__currBranches.add(branch)
            for line in newCov.lines(src_file):
                statement = (src_file, line)
                if statement not in self.__allStatements:
                    self.__allStatements.add(statement)
                    self.__newStatements.add(statement)
                    self.__newCurrStatements.add(statement)
                if statement not in self.__currStatements:
                    self.__currStatements.add(statement)
    
    
    def silenceCoverage(self):
        self.__cov._warn_no_data = False
    
    
    def internalReport(self):
        print("TSTL INTERNAL COVERAGE REPORT:")
        if self.__oldCovData is None:
            return
        for src_file in self.__oldCovData.measured_files():
            adata = self.__oldCovData.arcs(src_file)
            print(src_file, "ARCS:", len(adata), sorted(adata))
            for (f, a) in self.__allBranches:
                if f == src_file:
                    if a not in adata:
                        print("WARNING:", a, "VISITED BUT MISSING FROM COVERAGEDATA")
            for a in adata:
                if (src_file, a) not in self.__allBranches:
                    print(
                        "WARNING:",
                        a,
                        "IN COVERAGEDATA BUT NOT IN TSTL COVERAGE")
            ldata = list(set(self.__oldCovData.lines(src_file)))
            print(src_file, "LINES:", len(ldata), sorted(ldata))
            for (f, l) in self.__allStatements:
                if f == src_file:
                    if l not in ldata:
                        print("WARNING:", l, "VISITED BUT MISSING FROM COVERAGEDATA")
            for l in ldata:
                if (src_file, l) not in self.__allStatements:
                    print("WARNING", l, "IN COVERAGEDATA BUT NOT IN TSTL COVERAGE")
        for (f, l) in self.__allStatements:
            if f not in self.__oldCovData.measured_files():
                print("WARNING:", (f, l), "IS NOT IN COVERAGEDATA")
        print("TSTL BRANCH COUNT:", len(self.__allBranches))
        print("TSTL STATEMENT COUNT:", len(self.__allStatements))
    
    
    def cleanCov(self):
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
        if self.__oldCovData is None:
            self.__oldCovData = coverage.CoverageData()
        if self.__cov.get_data() is None:
            return
        self.__oldCovData.update(self.__cov.get_data())
        self.__cov.erase()
    
    
    def resetCov(self):
        self.__cov.erase()
        self.__oldCovData = None
        self.__allBranches = set()
        self.__allStatements = set()
        self.__newBranches = set()
        self.__newStatements = set()
        self.__currBranches = set()
        self.__currStatements = set()
        self.__newCurrBranches = set()
        self.__newCurrStatements = set()
    
    
    def report(self, filename):
        if self.__oldCovData is not None:
            self.__oldCovData.write_file(filename)
            self.__cov.combine([filename])
        outf = open(filename, 'w')
        r = -1
        try:
            r = self.__cov.report(morfs=self.__modules,
                                  file=outf, show_missing=True)
        finally:
            outf.close()
            return r
    
    
    def htmlReport(self, dir):
        if self.__oldCovData is not None:
            self.__oldCovData.write_file(dir + "/.tmpcov")
            self.__cov.combine([dir + "/.tmpcov"])
        r = -1
        try:
            r = self.__cov.html_report(
                morfs=self.__modules,
                directory=dir,
                title="TSTL Coverage Report",
                show_missing=True)
        finally:
            return r
    
    
    def allBranches(self):
        return self.__allBranches
    
    
    def allStatements(self):
        return self.__allStatements
    
    
    def currBranches(self):
        return self.__currBranches
    
    
    def currStatements(self):
        return self.__currStatements
    
    
    def newBranches(self):
        return self.__newBranches
    
    
    def newStatements(self):
        return self.__newStatements
    
    
    def newCurrBranches(self):
        return self.__newCurrBranches
    
    
    def newCurrStatements(self):
        return self.__newCurrStatements
    
    
    def startCoverage(self):
        self.__collectCov = True
    
    
    def stopCoverage(self):
        self.__collectCov = False
    
    
    def coversBranches(self, branches, catchUncaught=False, checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
    
    
    def coversStatements(self, statements, catchUncaught=False, checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            return True
        return coverPred
    
    
    def coversAll(
            self,
            statements,
            branches,
            catchUncaught=False,
            checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            return True
        return coverPred
    
    
    def coversMore(
            self,
            statements,
            branches,
            catchUncaught=False,
            checkProp=False):
        def coverPred(test):
            try:
                self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
            except KeyboardInterrupt as e:
                raise e
            except BaseException:
                pass
            cs = self.currStatements()
            for s in statements:
                if s not in cs:
                    return False
            cb = self.currBranches()
            for b in branches:
                if b not in cb:
                    return False
            for b in cb:
                if b not in branches:
                    return True
            for s in cs:
                if s not in statements:
                    return True
            return False
        return coverPred
    
    
    def coversSame(self, test, catchUncaught=False, checkProp=False):
        self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        return self.coversAll(
            self.currStatements(),
            self.currBranches(),
            catchUncaught=catchUncaught,
            checkProp=checkProp)
    
    
    def coversMoreThan(self, test, catchUncaught=False, checkProp=False):
        self.replay(test, catchUncaught=catchUncaught, checkProp=checkProp)
        return self.coversMore(
            self.currStatements(),
            self.currBranches(),
            catchUncaught=catchUncaught,
            checkProp=checkProp)
    
    
    def coverDecompose(
            self,
            test,
            verbose=False,
            catchUncaught=False,
            checkProp=False):
        (result, coverages) = self.replay(test, returnCov=True,
                                          catchUncaught=catchUncaught, checkProp=checkProp)
        tests = []
        coverages.reverse()
    
        allSCoverages = set([])
        allBCoverages = set([])
        for (s, b) in coverages:
            allSCoverages.update(set(s))
            allBCoverages.update(set(b))
    
        if verbose:
            print("ORIGINAL TEST OF LENGTH", len(test), "COVERS", len(
                allSCoverages), "STATEMENTS AND", len(allBCoverages), "BRANCHES")
    
        i = 1
        while (len(allSCoverages) != 0) or (len(allBCoverages) != 0):
            (sgoal, bgoal) = coverages[0]
            if verbose:
                print("CONSTRUCTING TEST #" + str(i), "WITH GOAL",
                      len(sgoal), "STATEMENTS AND", len(bgoal), "BRANCHES")
            t = self.reduce(
                test,
                self.coversAll(
                    sgoal,
                    bgoal,
                    catchUncaught=catchUncaught,
                    checkProp=checkProp),
                verbose=verbose)
            tests.append(t)
            self.replay(t, catchUncaught=catchUncaught, checkProp=checkProp)
            currS = set(self.currStatements())
            currB = set(self.currBranches())
            allSCoverages.difference_update(currS)
            allBCoverages.difference_update(currB)
            if verbose:
                print("NEW TEST OF LENGTH", len(t), "COVERS", len(
                    currS), "STATEMENTS AND", len(currB), "BRANCHES")
                print("REMAINING COVERAGE GOALS:", len(allSCoverages),
                      "STATEMENTS,", len(allBCoverages), "BRANCHES")
            newCoverages = []
            for (s, b) in coverages:
                newS = s.copy()
                newB = b.copy()
                newS.difference_update(currS)
                newB.difference_update(currB)
                if verbose and ((len(newS) != len(s)) or (len(newB) != len(b))):
                    print("GOAL WAS:", len(s), len(b))
                    print("NOW:", len(newS), len(newB))
                if (len(newS) != 0) or (len(newB) != 0):
                    newCoverages.append((newS, newB))
            coverages = newCoverages
            i += 1
        return tests
