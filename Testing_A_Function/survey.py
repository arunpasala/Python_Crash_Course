class AnonymousSurvey:
    """collect anonymous answers to a survey"""
    
    def __init__(self, question):
        """Store a question and prepare to store a response"""
        self.question = question
        self.response =[]
        
    def show_question(self):
        """show the survey questions"""
        print(self.question)
        
    
    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.response.append(new_response)
        
    def show_results(self):
        """Show all the responses that have beem given"""
        print("Survey result: ")
        for response in self.response:
            print(f"-{response}")
        