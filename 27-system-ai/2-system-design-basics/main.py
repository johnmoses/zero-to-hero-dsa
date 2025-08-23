# System Design Basics - Python example (Simulated Load Balancer)

class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server

if __name__ == "__main__":
    lb = LoadBalancer(['server1', 'server2', 'server3'])
    for _ in range(5):
        print(lb.get_server())
