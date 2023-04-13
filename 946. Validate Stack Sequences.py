# The basic idea is to iterate through the push and 
# pop arrays, and push elements onto the stack until 
# the top of the stack matches the current element in 
# the pop array, at which point we can 
# pop the element from the stack

def validateStackSequences(pushed, popped):
    st = []
    check = 0
    for x in pushed:
        st.append(x)
        while st and st[-1] == popped[check]:
            st.pop(-1)
            check+=1
    return check == len(pushed)