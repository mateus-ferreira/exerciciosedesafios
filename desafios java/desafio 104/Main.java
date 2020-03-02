class Main {
  public static void main(String[] args) {
    int x = 1;
    int y = 2;
    
    int z = x;
    x = y;
    y = z;

    System.out.println(x);
    System.out.println(y);

    x = 1;
    y = 2;

    x = x + y;
    y = x - y;
    x = x - y;

    System.out.println(x);
    System.out.println(y);
  }
}