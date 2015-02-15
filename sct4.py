from mpi4py import MPI
comm = MPI.COMM_WORLD
rank=comm.rank
size=comm.size
print 'Rank:',rank
print 'Node Count:',size
print 9**(rank+3)
