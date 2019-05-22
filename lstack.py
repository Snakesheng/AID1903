"""
栈的链式存储
重点代码
"""

#　自定义栈异常
class StackError(Exception):
    pass

n = 1000
x = 8888

# 创建结点类
class Node(object):
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next

class LStack:
    def __init__(self):
        #　标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,elem):
        self._top = Node(elem,self._top)

    def pop(self):
        if self._top is None:
            raise StackError("stack is empty")
        p = self._top
        self._top = p.next
        return p.val

    #　查看栈顶元素值
    def top(self):
        if self._top is None:
            raise StackError("stack is empty")
        return self._top.val

if __name__ == "__main__":
    st = LStack()
    print(st.is_empty()) #　判断是否为空
    st.push(10)
    st.push(20)
    print(st.top()) #　获取栈顶元素值
    st.push(30)
    while not st.is_empty():
        print(st.pop())








