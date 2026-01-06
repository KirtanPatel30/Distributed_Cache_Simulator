from sim.cluster import Cluster
from sim.workload import run_workload

if __name__ == "__main__":
    cluster = Cluster(
        num_nodes=4,
        replication_factor=2,
        eviction_policy="lru",
        capacity_per_node=200
    )

    run_workload(
        cluster=cluster,
        duration_s=5,
        rps=500,
        get_ratio=0.8
    )
