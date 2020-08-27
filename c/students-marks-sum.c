

//Complete the following function.

int marks_summation(int* marks, int number_of_students, char gender) {
  //Write your code here.
    int i,score=0;
    for (i=0; i<number_of_students; i++) {
      if(gender=='b'){
        if(i%2==0)
            score+=marks[i];
      }
      else {
      if(i%2!=0)
            score+=marks[i];
      }

  }
  return score;
}

