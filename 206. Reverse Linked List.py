
class ListNode:
    def __init__(self, x):
        self.val=x
        self.next=None

head=ListNode(1)
a2=ListNode(2)
a3=ListNode(3)
a4=ListNode(4)
a5=ListNode(5)

head.next=a2
a2.next=a3
a3.next=a4
a4.next=a5

def reverseList(head: ListNode) -> ListNode:
   #链表为空或者只有一个节点：
    if head==None or head.next==None: 
        return head
       
   #链表有两个节点或以上：
    temp=head.next.next
    head,head.next=head.next,head
    head.next.next=None

    while temp and temp.next:
        temp,head,head.next=temp.next,temp,head
    head,head.next=temp,head
    return head

head=reverseList(head)

while head.next:
    print(head.val)
    head = head.next
print(head.val)