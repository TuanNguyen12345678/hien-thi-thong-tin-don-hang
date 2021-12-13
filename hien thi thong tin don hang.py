# HIỂN THỊ THÔNG TIN ĐƠN HÀNG:
import math
def donhang():
    try:
        gia=float(input('NHẬP SỐ TIỀN KHÁCH MUA HÀNG: '))
        if 0<gia<75:
            print('KHÔNG ĐƯỢC GIẢM GIÁ')
        elif 75<=gia<100:
            print('ĐƯỢC GIẢM 15$ CÒN: ',gia-15,"$")
        elif 100<=gia<150:
            print('ĐƯỢC GIẢM 25$ CÒN: ',gia-25,"$")
        elif gia>=150:
            print('ĐƯỢC GIẢM 50$ CÒN: ',gia-50,"$")
    except:
        print('NHẬP ĐỊNH DẠNG CHƯA ĐÚNG')
if __name__=="__main__":
    donhang()