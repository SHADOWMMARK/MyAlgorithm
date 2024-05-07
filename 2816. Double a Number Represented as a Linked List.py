def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    fake = ListNode(0,head)
    temp = head
    vals = []
    while temp:
        vals.append(temp.val)
        temp = temp.next
    ans_list = [0]*len(vals)
    k = 0
    for i, v in enumerate(vals[::-1]):
        if v*2 + k >= 10:
            ans_list[i] = v*2 + k - 10
            k = 1
        else:
            ans_list[i] = v*2 + k
            k = 0
    if k == 1:
        ans_list.append(1)
        temp = fake
    else:
        temp = fake.next

    for i in ans_list[::-1]:
        temp.val = i
        temp = temp.next
    if len(ans_list)>len(vals):
        return fake
    else:
        return fake.next
