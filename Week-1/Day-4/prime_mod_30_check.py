def primes(n): #Sieve of Eratosthenes
	prime=[]
	sieve=[True]*(n+1)
	prime.append(1)
	for p in range (2,n+1,1):
		if sieve[p]:
			prime.append(p)
			for i in range(p*p,n+1,p):
				sieve[i]=False
	# print sieve
	return prime

lst = primes(1000000)
print 127%30 in lst