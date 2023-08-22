class Books:
    data=[
        {"id":101,"name":"The Guide","author":"R.K Narayan","theme":"fiction","year":1958},
        {"id":102,"name":"The One You Cannot Have","author":"Preeti Shenoy","theme":"love","year":1988},
        {"id":103,"name":"The Game World Trilogy","author":"Samit Basu","theme":"science fiction","year":1990},
        {"id":104,"name":"The Devils wind","author":"Manohar Malgokar","theme":"historical","year":1858},
        {"id":105,"name":"Dork Trilogy","author":"Einstein Vargese","theme":"humour","year":1877},
        
    ]
    def get(self):
        return self.data
    # def retrieve(self,theme):
    #     return[b for b in self.data if b.theme==theme]
    def retrieve(self,id):
        return[b for b in self.data if b.get("id")==id] 
    def post(self,obj):
        self.data.append(obj)
    def destroy(self,id):
        obj=[b for b in self.data if b.get("id")==id] 
        self.data.remove(obj)    

obj=Books() 
print(obj.get())
# print(obj.retrieve("fiction"))
print(obj.retrieve(103)) 
book={"id":106,"name":"Macbeth","author":"william shekspere","theme":"crime thriller","year":1779}
obj.post(book)
print(obj.get())
obj.destroy(5)
print(obj.get())

 
