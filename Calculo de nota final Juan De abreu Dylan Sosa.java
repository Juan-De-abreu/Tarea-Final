/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.tareaprogra;

/**
 *
 * @author PC
 */
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Cual es el nombre del alumno: ");
        String alumno = scanner.nextLine();
 
        double notaalumno = Nota_final(scanner);
        if (notaalumno > 9) {
            System.out.println("El alumno " + alumno + " ha aprobado con un total de: " + notaalumno);
        } else {
            System.out.println("El alumno " + alumno + " ha reprobado con un total de: " + notaalumno);
        }
    }
 
    public static double Nota_final(Scanner scanner) {
        double nota = 0;
        System.out.print("Cantidad de notas a calcular: ");
        int cantidad = scanner.nextInt();
        for (int i = 0; i < cantidad; i++) {
            System.out.print("Introduce la nota numero " + (i + 1) + ": ");
            int notaalumno = scanner.nextInt();
            nota += notaalumno;
        }
        double notatotal = nota / cantidad;
        return notatotal;
    }
}