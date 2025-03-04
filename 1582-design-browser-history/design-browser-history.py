class BrowserHistory:

    class Node:
        def __init__(self, url: str):
            self.url = url
            self.next = None
            self.prev = None

    def __init__(self, homepage: str):

        self.curr = self.Node(homepage)

    def visit(self, url: str) -> None:
        
        new_page = self.Node(url)
        self.curr.next = new_page
        new_page.prev = self.curr
        self.curr = new_page


    def back(self, steps: int) -> str:

        while steps > 0:
            if self.curr.prev:
                self.curr = self.curr.prev
                steps -= 1
            else:
                break

        return self.curr.url

    def forward(self, steps: int) -> str:

        while steps > 0:
            if self.curr.next:

                self.curr = self.curr.next
                steps -= 1

            else:
                break

        return self.curr.url
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)