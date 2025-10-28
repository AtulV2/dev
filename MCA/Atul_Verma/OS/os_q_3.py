import psutil

memory = psutil.virtual_memory()
print(f"Totla Memory: {memory.total/(1024**2):.2f} MB")         
print(f"Used Memory {memory.used/(1024**2):.2f} MB")           
print(f"Availabel Memory {memory.available/(1024**2):.2f} MB")  
