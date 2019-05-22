"""
栈的顺序存储结构
重点代码
"""
import os  # Tom



import threading  # Jame

#　自定义栈异常
class StackError(Exception):
    pass

#　基于列表实现顺序栈
class SStack:
    def __init__(self):
        #　约定列表的最后一个元素为栈顶
        self._elems = []

    def top(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems[-1]

    #　判断栈是否为空
    def is_empty(self):
        return self._elems == []

    #　入栈
    def push(self,elem):
        self._elems.append(elem)

    #　出栈
    def pop(self):
        if not self._elems:
            raise StackError("stack is empty")
        return self._elems.pop()


if __name__ == "__main__":
    st = SStack() #　初始化栈
    # print(st.top())
    print(st.is_empty())
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
