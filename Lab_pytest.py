import pytest
import pandas as pd

def children(data):
    count = {'C': 0, 'Q': 0, 'S': 0}
    max_age = {'C': 0, 'Q': 0, 'S': 0}
    children = 0
    
    for index, row in data.iterrows():
        if pd.notna(row['Age']) and row['Age'] < 18 and row['Survived'] == 0:
            embarked = row['Embarked']
            
            if embarked in count:
                count[embarked] += 1
                children +=1
                
            if embarked in ['C', 'Q', 'S'] and row['Age'] > max_age[embarked]:
                max_age[embarked] = int(row['Age'])
    
    return count, children, max_age  

class TestTitanicAnalysis:
    
    def test_1(self):
        """Данные всех портов"""
        test_data = pd.DataFrame({
            'Age': [5, 10, 15, 8, 12],
            'Survived': [0, 0, 0, 0, 0],
            'Embarked': ['C', 'Q', 'S', 'C', 'Q'],
            'Pclass': [1, 2, 3, 1, 2]
        })
        
        counts, total, max_ages = children(test_data)
        
        assert counts['C'] == 2
        assert counts['Q'] == 2
        assert counts['S'] == 1
        assert total == 5
        assert max_ages['C'] == 8
        assert max_ages['Q'] == 12
        assert max_ages['S'] == 15
    
    def test_2(self):
        """Нет погибших детей"""
        test_data = pd.DataFrame({
            'Age': [5, 10, 15],
            'Survived': [1, 1, 1],  
            'Embarked': ['C', 'Q', 'S'],
            'Pclass': [1, 2, 3]
        })
        
        counts, total, max_ages = children(test_data)
        
        assert counts['C'] == 0
        assert counts['Q'] == 0
        assert counts['S'] == 0
        assert total == 0
        assert max_ages['C'] == 0
        assert max_ages['Q'] == 0
        assert max_ages['S'] == 0
    
    
    def test_3(self):
        """Макс возраст по классам"""
        test_data = pd.DataFrame({
            'Age': [17, 5, 15, 8, 12],
            'Survived': [0, 0, 0, 0, 0],
            'Embarked': ['C', 'Q', 'S', 'C', 'Q'],
            'Pclass': [1, 1, 1, 2, 3]  
        })
        
        counts, total, max_ages = children(test_data)
        
        assert max_ages['C'] == 17
        assert max_ages['Q'] == 12
        assert max_ages['S'] == 15
if __name__ == "__main__":

    pytest.main([__file__, "-v"])        
