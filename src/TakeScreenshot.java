import java.awt.Rectangle;
import java.awt.Toolkit;
import java.awt.Robot;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class TakeScreenshot {
    public static final long serialVersionUID = 1L;

    public static void Take_Screenshot(String now) {
        try {
            Robot r = new Robot();

            // It saves screenshot to desired path
            String path = "D://Shots/" + now + ".png";

            // Used to get ScreenSize and capture image
            Rectangle capture =
                    new Rectangle(Toolkit.getDefaultToolkit().getScreenSize());
            BufferedImage Image = r.createScreenCapture(capture);
            ImageIO.write(Image, "png", new File(path));
            // System.out.println("Screenshot saved New");
        }
        catch (Exception ex) {
            System.out.println(ex);
        }
    }
}