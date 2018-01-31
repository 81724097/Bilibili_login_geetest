import time
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

class slider_cracker(object):
    def __init__(self,driver):
        self.driver = driver
        self.driver.maximize_window() #最大化窗口

    def get_true_image(self,slider_xpath=r'//*[@id="gc-box"]/div/div[3]/div[1]'):
        element = self.driver.find_element_by_xpath(slider_xpath)
        ActionChains(self.driver).move_to_element(element).perform()
        time.sleep(1)
        true_image = self.get_img('true_image.png')
        return true_image

    def get_img(self,img_name,img_xpath=r'//*[@id="gc-box"]/div/div[1]/div[2]/div[1]/a[2]'):#260*116
        screen_shot = self.driver.save_screenshot('slider_screenshot.png')
        image_element = self.driver.find_element_by_xpath(img_xpath)
        left = image_element.location['x']
        top = image_element.location['y']
        right = image_element.location['x'] + image_element.size['width']
        bottom = image_element.location['y'] + image_element.size['height']
        image = Image.open('slider_screenshot.png')
        image = image.crop((left, top, right, bottom))
        image.save(img_name)
        return image

    def analysis(self,true_image,knob_xpath=r'//*[@id="gc-box"]/div/div[3]/div[2]'):
        img1 = Image.open('true_image.png')
        slider_element = self.driver.find_element_by_xpath(knob_xpath)
        ActionChains(self.driver).click_and_hold(slider_element).perform()
        img2 = self.get_img('img2.png')
        img1_width,img1_height = img1.size
        img2_width,img2_height = img2.size
        left = 0
        flag = False

        for i in range(65, img1_width):
            for j in range(0,img1_height):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    flag = True
                    break
            if flag:
                break
        '''if left == 45:
            left -= 2'''
        left = left-5
        return left

    def is_pixel_equal(self, img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0] < 60) and abs(pix1[1] - pix2[1] < 60) and abs(pix1[2] - pix2[2] < 60)):
            return True
        else:
            return False

    def drag_and_drop(self, x_offset=0, y_offset=0, knob_xpath=r'//*[@id="gc-box"]/div/div[3]/div[2]'):
        """拖拽滑块
        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :element_class: 滑块网页元素CSS类名
        """
        knob_element = self.driver.find_element_by_xpath(knob_xpath)
        ActionChains(self.driver).drag_and_drop_by_offset(knob_element, x_offset, y_offset).perform()
        # 这个延时必须有，在滑动后等待回复原状
        time.sleep(2)

    def crack(self):
        true_image = self.get_true_image()
        x_offset = self.analysis(true_image)
        print(x_offset)
        self.drag_and_drop(x_offset=x_offset,y_offset=30)




