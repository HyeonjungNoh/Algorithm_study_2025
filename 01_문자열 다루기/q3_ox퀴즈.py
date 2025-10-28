def solution(quiz):
    answer = []
    

    for formula in quiz:
        
       parts = formula.split()
       
       if parts[1] == '+':
           an_r = int(parts[0]) + int(parts[2])
           if an_r == int(parts[4]):
               answer.append("O")
           else:
               answer.append("X")
       else:
           an_r = int(parts[0]) - int(parts[2])
           if an_r == int(parts[4]):
               answer.append("O")
           else:
               answer.append("X")
           
           
            
    return answer


quiz = ["3 - 4 = -3", "5 + 6 = 11"]
print(solution(quiz))