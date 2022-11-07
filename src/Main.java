import java.io.IOException;

import java.time.format.DateTimeFormatter;
import java.time.LocalDateTime;

class Main extends Thread {
    public void run() {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("HH-mm---ss dd-MM-yyyy");
        while(true) {
            try {
                LocalDateTime now = LocalDateTime.now();
                TakeScreenshot.Take_Screenshot(dtf.format(now));
                SmilePlease.Take_Selfie();
                Thread.sleep(1000);
            }
            catch (InterruptedException E) {
                System.out.println(E);
            }
        }
    }
    public static void main(String[] args) {
        Main t = new Main();
        t.start();
    }
}
