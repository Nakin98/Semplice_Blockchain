
#Red-Blockchain

import hashlib  

class RedBlock:
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash  #Riferimento blocco precedente
        self.transaction_list = transaction_list        #Lista di transazioni nel blocco

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()




class Blockchain:
    def __init__(self):
        self.chain = []   #Catena di blocchi inizialmente vuota
        self.generate_genesis_block()  #Primo blocco della blockchain


    def generate_genesis_block(self):
        self.chain.append(RedBlock("0",["Genesis Block"]))


    #Possiamo creare blocchi semplicemente inserendo le transazioni
    #In questa funzione
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block_hash()
        self.chain.append(RedBlock(previous_block_hash, transaction_list))
    

    #Stampa la blockchain
    def display_chain(self): 
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i+1}: {self.chain[i].block_hash}\n")
    

    #Ultimo elemento 
    def last_block_hash(self):
        last = self.chain[-1]
        return last.block_hash 




"""   ----- TEST ----- """


myblockchain = Blockchain()

#Transazioni
t1 = "Marco ha inviato 3coin a Maria"
t2 = "Francesca ha inviato 2.5coin a Benedetta"
t3 = "Elena ha inviato 4coin a Paolo"
t4 = "Manuel ha inviato 4.5coin a Giovanni"
# .....


myblockchain.create_block_from_transaction([t1,t2])
myblockchain.create_block_from_transaction([t3,t4])
myblockchain.display_chain()


"""
#Output 1

Data 1: Genesis Block - 0
Hash 1: 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e

Data 2: Marco ha inviato 3coin a Maria - Francesca ha inviato 2.5coin a Benedetta - 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e
Hash 2: 5d9d294d3586d15680bddb01bfae6bf210f613187834fcd7be79c3012b366539

Data 3: Elena ha inviato 4coin a Paolo - Manuel ha inviato 4.5coin a Giovanni - 5d9d294d3586d15680bddb01bfae6bf210f613187834fcd7be79c3012b366539
Hash 3: 4e9647771bfaaf22db9d8ceb38a9f9b2722f5526c65dfaa678bfe887950740bb

"""
print("\n\n\n")

myblockchain2 = Blockchain()

#Cambiamo il nome di Marco in Mark e vediamo come cambia la blockchain
t1 = "Mark ha inviato 3coin a Maria"
t2 = "Francesca ha inviato 2.5coin a Benedetta"
t3 = "Elena ha inviato 4coin a Paolo"
t4 = "Manuel ha inviato 4.5coin a Giovanni"
# .....


myblockchain2.create_block_from_transaction([t1,t2])
myblockchain2.create_block_from_transaction([t3,t4])
myblockchain2.display_chain()



"""
Output 2
Data 1: Genesis Block - 0
Hash 1: 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e

Data 2: Mark ha inviato 3coin a Maria - Francesca ha inviato 2.5coin a Benedetta - 39331a6a2ea1cf31a5014b2a7c9e8dfad82df0b0666e81ce04cf8173cc5aed3e
Hash 2: 97ac56c79f62408e5cf4d1a305bd937143035f31ff820d7caa8385c88c9c6478

Data 3: Elena ha inviato 4coin a Paolo - Manuel ha inviato 4.5coin a Giovanni - 97ac56c79f62408e5cf4d1a305bd937143035f31ff820d7caa8385c88c9c6478
Hash 3: aa12c28de76a4c17430090cf672b57fc91c86f4e86f08ee8050e3577e9b796ff

"""