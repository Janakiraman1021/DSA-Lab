import java.io.*;
import java.util.*;

class Record {
    static Scanner input = new Scanner(System.in);
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int roll;
    String name;

    void insert() {
        try {
            System.out.println("\nEnter Roll No:");
            roll = input.nextInt();
            System.out.println("\nEnter Name:");
            name = br.readLine();
            FileOutputStream fout = new FileOutputStream("Student.txt", true);
            byte[] buff = name.getBytes();
            fout.write((char) roll);
            fout.write('\n');
            fout.write(buff);
            fout.write('\n');
            fout.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    void delete(int r) {
        try {
            FileInputStream fin = new FileInputStream("student.txt");
            FileOutputStream fout = new FileOutputStream("temp.txt");
            while (true) {
                int a = fin.read();
                if (a == -1)
                    break;
                if (a != r) {
                    fout.write((byte) a);
                    a = fin.read();
                    fout.write(a);
                    while (true) {
                        a = fin.read();
                        if (a == '\n')
                            break;
                        fout.write(a);
                    }
                    fout.write(a);
                } else {
                    a = fin.read();
                    do {
                        a = fin.read();
                    } while (a != '\n');
                }
            }
            fin.close();
            fout.close();
            File f = new File("student.txt");
            File f1 = new File("temp.txt");
            if (f.delete())
                f1.renameTo(new File("student.txt"));
            else
                System.out.println("Error");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    void showdata(int r) {
        try {
            FileInputStream fin = new FileInputStream("student.txt");
            while (true) {
                int a = fin.read();
                if (a == -1)
                    break;
                if (a == r) {
                    System.out.println("Roll No: " + a);
                    a = fin.read();
                    System.out.println("Name: ");
                    do {
                        a = fin.read();
                        System.out.print((char) a);
                    } while (a != '\n');
                } else {
                    do {
                        a = fin.read();
                    } while (a != '\n');
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    void show() {
        try {
            FileInputStream fin = new FileInputStream("student.txt");
            while (true) {
                int a = fin.read();
                if (a == -1)
                    break;
                System.out.println("Roll No: " + a);
                a = fin.read();
                System.out.println("Name: ");
                do {
                    a = fin.read();
                    System.out.print((char) a);
                } while (a != '\n');
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}

public class Student extends Record {
    public static void main(String args[]) {
        try {
            while (true) {
                System.out.println("\nEnter your choice:");
                System.out.println("1: Insert.");
                System.out.println("2: Delete.");
                System.out.println("3: View record.");
                System.out.println("4: View All.\n");
                int choice = Record.input.nextInt();
                Record r = new Record();
                switch (choice) {
                    case 1:
                        r.insert();
                        break;
                    case 2:
                        System.out.println("Enter roll no.: ");
                        int roll = Record.input.nextInt();
                        r.delete(roll);
                        break;
                    case 3:
                        System.out.println("Enter roll no.: ");
                        roll = Record.input.nextInt();
                        r.showdata(roll);
                        break;
                    case 4:
                        r.show();
                        break;
                    default:
                        System.out.println("Invalid Entry!");
                        break;
                }
            }
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
