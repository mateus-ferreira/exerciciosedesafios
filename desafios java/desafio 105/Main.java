class Main {
  public static void main(String[] args) {
    int lista[]=new int[1000];

    for(int i=0; i<1000; i++){
      if(i%2==0){
        lista[i] = i;
      }
    }
    for(int i=0; i<1000; i++){
      System.out.println(lista[i]);
    }
    

    for(int i = 1; i<999999; i++){
      if(i%5==0){
        System.out.println(i);
        break;
      }
    }
  }
}