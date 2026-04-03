Dollar=86.16176
print(f"1$ is approximately equivalent to {Dollar:.2f}₹")
# we can also write it in another way:
Fact="1{0} is approximately equivalent to {2:.2f}{1}"
C1="$"
C2="₹"
Relation=86.16176
print(Fact.format(C1,C2,Relation))
# use of f string makes our work easier :)
print(f"1{C1} is approximately equivalent to {Relation:.2f}{C2}")

