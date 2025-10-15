
from listNode import ListNode
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1:ListNode, list2:ListNode):
        """
        Funkcja łączy dwie posortowane listy jednokierunkowe (ListNode) 
        w jedną posortowaną listę i zwraca jej początek.
        """
        # Tworzymy pomocniczy węzeł 'dummy', który pozwala nam łatwo budować nową listę
        dummy = ListNode(0)
        # 'current' to wskaźnik, który będzie przesuwał się w nowej liście
        current = dummy

        # Pętla działa dopóki obie listy mają elementy
        while list1 and list2:
            # Porównujemy aktualne wartości węzłów
            if list1.val < list2.val:
                # Wstawiamy mniejszy węzeł do nowej listy
                current.next = list1
                # Przesuwamy wskaźnik w list1
                list1 = list1.next
            else:
                # W przeciwnym wypadku wstawiamy węzeł z list2
                current.next = list2
                # Przesuwamy wskaźnik w list2
                list2 = list2.next

            # Przesuwamy wskaźnik 'current' w nowej liście
            current = current.next

        # Po wyjściu z pętli jedna z list może mieć jeszcze elementy
        # Doklejamy resztę tej listy na końcu nowej listy
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Zwracamy początek nowej listy (pomijamy dummy)
        return dummy.next
    
s = Solution()
print(s.mergeTwoLists(ListNode.to_listnode([1,2,4]),ListNode.to_listnode([1,3,4])))

    
