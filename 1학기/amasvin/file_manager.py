import pickle

class FileManager:  # 클래스를 만들면 생성자느 ㄴ무조건 있어야해요
    def __init__(self, filename):
        self.filename = filename

    def save(self, data):
        f = open(self.filename, "wb")
        pickle.dump(data, f)
        f.close()

    def load(self):
        try:
            f = open(self.filename, "rb")
            data = pickle.load(f)
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError
        return data
