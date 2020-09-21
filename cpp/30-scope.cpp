
    Difference(vector<int> elements){
        this->elements=elements;
        this->maximumDifference=0;
    }
	// Add your code here
    int computeDifference(void){
        for (int i=0; i<elements.size(); i++) {
            for (int j=i+1; j<elements.size(); j++) {
                if(abs(elements[i]-elements[j])>maximumDifference)
                    maximumDifference=abs(elements[i]-elements[j]);
            }
        }
        return maximumDifference;
    }
