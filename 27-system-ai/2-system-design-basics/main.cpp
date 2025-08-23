// System Design Basics - C++ example (Simulated Load Balancer)

#include <iostream>
#include <vector>
#include <string>

class LoadBalancer {
    std::vector<std::string> servers;
    int index = 0;
public:
    LoadBalancer(const std::vector<std::string>& servers) : servers(servers) {}

    std::string getServer() {
        std::string server = servers[index];
        index = (index + 1) % servers.size();
        return server;
    }
};

int main() {
    LoadBalancer lb({"server1", "server2", "server3"});
    for (int i = 0; i < 5; i++) {
        std::cout << lb.getServer() << std::endl;
    }
    return 0;
}
