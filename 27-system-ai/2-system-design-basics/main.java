// System Design Basics - Java example (Simulated Load Balancer)

class Main {
    static class LoadBalancer {
        private String[] servers;
        private int index = 0;

        public LoadBalancer(String[] servers) {
            this.servers = servers;
        }

        public String getServer() {
            String server = servers[index];
            index = (index + 1) % servers.length;
            return server;
        }
    }

    public static void main(String[] args) {
        LoadBalancer lb = new LoadBalancer(new String[]{"server1", "server2", "server3"});
        for (int i = 0; i < 5; i++) {
            System.out.println(lb.getServer());
        }
    }
}
