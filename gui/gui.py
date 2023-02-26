# 2023/1/28 17:49
# 你好，夜嗨大帅比

# QT5
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QHBoxLayout, QVBoxLayout, QLineEdit, QCheckBox, \
    QHeaderView, QMenu, QAbstractItemView
from PyQt5.QtWidgets import QPushButton, QListWidget, QLabel,QTableWidgetItem,QTableWidget,QStackedWidget,QListWidgetItem
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl

# 网站分析
import qdarkstyle
import sys
import re

# 数据库
from data_save.text import DB




class MainWindow(QWidget):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)

        self.regular = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        self.wangzhi = re.compile('[a-zA-z]+://[^\s]*')


        self.setWindowIcon(QIcon('../image/mao.jpg'))
        # 文本输入空间 ui3
        self.txt_text = None


        # 窗体标题
        self.setWindowTitle("Puat")
        # 窗体尺寸
        self.resize(1080,480)


        # 窗体位置
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        # 创建布局
        layout = QHBoxLayout()
        layout.setObjectName("layout")

        self.list_bar = self.list_bar()
        self.stack_conten = self.stack_conten()
        layout.addWidget(self.list_bar)
        layout.addWidget(self.stack_conten)
        layout.setStretch(0,2)
        layout.setStretch(1,8)
        layout.setSpacing(-10)
        # 给窗体设置元素的排列方式
        self.setLayout(layout)

        layout.setContentsMargins(0,0,0,0)
        self.list_bar.currentRowChanged.connect(self.display)

    # List_bar
    def list_bar(self):
        list_right_bar = QListWidget()

        list_right_bar.setFrameShape(QListWidget.NoFrame)

        one_item = QListWidgetItem(QIcon("../image/house.svg"), "  Home", list_right_bar)
        two_item = QListWidgetItem(QIcon("../image/info-square.svg"), "  Layer", list_right_bar)
        three_item = QListWidgetItem(QIcon("../image/search-heart-fill.svg"), "  Exploit", list_right_bar)


        list_right_bar.insertItem(1, one_item)
        list_right_bar.insertItem(2, two_item)
        list_right_bar.insertItem(1, three_item)

        return list_right_bar

        # 创建三个小控件
    def stack_conten(self):
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()

        stack = QStackedWidget()
        stack.addWidget(self.stack1)
        stack.addWidget(self.stack2)
        stack.addWidget(self.stack3)

        return stack


    def stack1UI(self):
        stack1UI = QVBoxLayout()
        stack1UI.setObjectName("stack1")

        label_image = QLabel()
        label_text = QLabel()
        label_text.setObjectName("label_text")
        label_image.setObjectName("label_image")
        # label_image.setStyleSheet()
        pixmap = QPixmap("../image/OIP.jpg")
        pix = pixmap.scaled(QSize(1000, 500), Qt.KeepAspectRatio)
        label_image.setPixmap(pix)
        label_image.setScaledContents(True)
        label_image.setAlignment(Qt.AlignCenter)

        # label_text.setText("Puat V0.1")
        # label_text.setAlignment(Qt.AlignCenter)
        stack1UI.addWidget(label_image)
        # stack1UI.addWidget(label_text)
        stack1UI.addLayout(self.foot_bar())

        stack1UI.setContentsMargins(0,0,0,0)

        self.stack1.setLayout(stack1UI)

    def stack2UI(self):
        stack2UI = QVBoxLayout()

        top_bar = QHBoxLayout()
        content_area = QVBoxLayout()

        label = QLabel("域名")
        self.edit_ui2 = edit = QLineEdit()
        check_box = QCheckBox()
        edit.setPlaceholderText("请输入URL")
        # check_box.setText("是否使用ssl")
        check_box.setChecked(False)

        start_run = QPushButton("开始搜索")

        start_run.clicked.connect(self.event_start_run_url_coll)

        top_bar.addWidget(label)
        top_bar.addWidget(edit)
        # top_bar.addWidget(check_box)
        top_bar.addWidget(start_run)

        table_widget2 = QTableWidget(0,4)
        table_widget2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        stack2UI.setContentsMargins(0,0,0,0)
        # stack2UI.setSpacing(0)
        self.table_widget2 = table_widget2
        table_hearder = [
            {"field": "eid", "text": "域名", },
            {"field": "title", "text": "解析IP", },
            {"field": "author", "text": "网站状况", },
            {"field": "publish_time", "text": "来源", },
        ]


        for idx, info in enumerate(table_hearder):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget2.setHorizontalHeaderItem(idx,item)


        content_area.addWidget(table_widget2)

        stack2UI.addLayout(top_bar)
        stack2UI.addLayout(content_area)
        stack2UI.addLayout(self.foot_bar())


        table_widget2.setContextMenuPolicy(Qt.CustomContextMenu)
        table_widget2.customContextMenuRequested.connect(self.table_right_menu2)


        self.stack2.setLayout(stack2UI)



    def stack3UI(self):
        ## 文本输入
        H_bar = QHBoxLayout()
        label = QLabel("Input")
        txt_text = QLineEdit()
        txt_text.setPlaceholderText("请输入网址，例如：www.baidu.com; 或者要查询的组件漏洞,例如：Ubuntu")
        txt_text.setStyleSheet('QLineEdit{ background-color: rgba(255,240,255,120); }QLineEdit:focus{background-color: rgb(255,255,255)}')
        self.txt_text = txt_text

        ## 搜索按钮
        btn_search = QPushButton("指纹搜索")

        btn_search.clicked.connect(self.event_sec_click)

        # 3.文本空间加入模块
        ## 文本区加入整个模块
        H_bar.addWidget(label)
        H_bar.addWidget(txt_text)
        H_bar.addWidget(btn_search)
        # 创建右侧整体布局
        content_bar = QVBoxLayout()

        # 表格创建
        table_widget = QTableWidget(0, 8)
        table_widget.setObjectName("stack3table")
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table_widget = table_widget

        table_hearder = [
            {"field": "eid", "text": "Eid", },
            {"field": "title", "text": "Title", },
            {"field": "author", "text": "Author", },
            {"field": "publish_time", "text": "Publish_time", },
            {"field": "platform", "text": "Platform", },
            {"field": "type", "text": "Type", },
            {"field": "exploit_url", "text": "Exp_url", },
            {"field": "download_url", "text": "Down_url", },
        ]

        for idx, info in enumerate(table_hearder):
            item = QTableWidgetItem()
            item.setText(info['text'])
            table_widget.setHorizontalHeaderItem(idx, item)

        db = DB()
        result = db.search_all()

        # 获取数据库中的数据,并在表格中显示
        current_row_count = table_widget.rowCount()

        self.content_to_table(result, current_row_count)

        # H_bar的文本区和搜索按钮的Layout 加入content_bar 之上
        content_bar.addLayout(H_bar)

        # 增加表格区域到布局中
        content_bar.addWidget(table_widget)

        # 加入底部栏
        content_bar.addLayout(self.foot_bar())

        table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        table_widget.customContextMenuRequested.connect(self.table_right_menu3)
        # 整体加入第三个布局
        content_bar.setContentsMargins(0, 0, 0, 0)
        self.stack3.setLayout(content_bar)

    # 用来切换那个widget 这里的self.stack_conten 必须是在上面的，在函数中创建后返回 连接不到
    def display(self,i):
        self.stack_conten.setCurrentIndex(i)



    def table_right_menu2(self, pos):

        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        # 只有选中一行时,才支持右键
        selected_item_list = self.table_widget2.selectedItems()
        if len(selected_item_list) == 0:
            return

        menu = QMenu()
        item_copy = menu.addAction("复制域名")
        item_open = menu.addAction("打开网站")
        action = menu.exec_(self.table_widget2.mapToGlobal(pos))

        if action == item_copy:
            # 复制当前域名
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_item_list[0].text())
        if action == item_open:
            QDesktopServices.openUrl(QUrl(selected_item_list[0].text()))


    def table_right_menu3(self, pos):
        # 只有选中一行时,才支持右键
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        selected_item_list = self.table_widget.selectedItems()
        if len(selected_item_list) == 0:
            return

        menu = QMenu()
        item_copy_exp_url = menu.addAction("复制详情域名")
        item_copy_down = menu.addAction("复制下载域名")
        item_open_exp_url = menu.addAction("打开详情网站")
        action = menu.exec_(self.table_widget.mapToGlobal(pos))

        if action == item_copy_exp_url:
            # 复制当前域名
            clipboard = QApplication.clipboard()
            clipboard.setText(selected_item_list[6].text())

        if action == item_copy_down:
            clipboard1 = QApplication.clipboard()
            clipboard1.setText(selected_item_list[7].text())

        if action == item_open_exp_url:
            QDesktopServices.openUrl(QUrl(selected_item_list[6].text()))

    # 每个页面的 foot 栏
    def foot_bar(self):
        # 底部的信息栏
        foot_bar = QHBoxLayout()
        foot_bar.setObjectName("foot")

        # author
        foot_content_author = QLabel("By: Yeahii")
        # version
        foot_content_version = QLabel("v1.0")
        # 底部信息
        foot_bar.addWidget(foot_content_author)
        foot_bar.addStretch()
        foot_bar.addWidget(foot_content_version)
        return foot_bar

    # 搜索按钮事件
    def event_sec_click(self):
        # 获取文本框中的内容
        db = DB()
        text = self.txt_text.text()
        text = text.strip()
        if not text:
            result = db.search_all()
            # 把行数清零
            self.table_widget.setRowCount(0)
            # 把内容全部清除，为下面更新数据做准备
            self.table_widget.clear()
            current_row_widget = self.table_widget.rowCount()
            self.table_widget.clearContents()
            self.content_to_table(result,current_row_widget)
            return

        from utils.wapp_thread import WappThreads
        if self.regular.match(text) or self.wangzhi.match(text):
            self.wapp_thread = WappThreads(self,text)
            self.wapp_thread.success.connect(self.info_poc_success)
            self.wapp_thread.start()
            pass
        else:
            result1 = db.search_all(text)

            # 把行数清零
            self.table_widget.setRowCount(0)
            # 把内容全部清除，为下面更新数据做准备
            self.table_widget.clear()
            current_row_count = self.table_widget.rowCount()

            self.table_widget.clearContents()
            self.content_to_table(result1,current_row_count)


    def content_to_table(self,result,current_row_count):
        for row_list in result:
            self.table_widget.insertRow(current_row_count)
            # 写入数据
            for i, ele in enumerate(row_list):
                cell = QTableWidgetItem(str(ele))
                # 设置鼠标悬浮单元格时，显示单元格中的内容
                cell.setToolTip(str(ele))
                # 表格内容不能被修改
                if i in [0, 1, 2, 3, 4, 5]:
                    cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                self.table_widget.setItem(current_row_count, i, cell)

            current_row_count += 1
        pass

    # 界面2的点击事件
    def event_start_run_url_coll(self):
        """
        读取输入的内容，并判断是否有输入
        然后创建子线程进行信号的传输
        :return:
        """
        text = self.edit_ui2.text()
        text = text.strip()
        if not text:
            return

        from utils.threads import NewTaskThread
        # self.thread = NewTaskThread(self,current_row_count,text)
        self.thread = NewTaskThread(self,url=text)
        self.thread.success.connect(self.init_table_success)
        self.thread.start()


    # 界面2响应事件 响应信号返回的值,进行数据填充
    def init_table_success(self,ip,url):
        # 更新url
        current_row_count = self.table_widget2.rowCount()
        self.table_widget2.insertRow(current_row_count)
        new_row_list = [url,ip,200,"枚举"]

        for i,ele in enumerate(new_row_list):
            cell = QTableWidgetItem(str(ele))
            cell.setToolTip(str(ele))
            self.table_widget2.setItem(current_row_count,i,cell)
    # 界面3 Url响应事件
    def info_poc_success(self,cms_result:list):
        # 把行数清零
        self.table_widget.setRowCount(0)
        # 把内容全部清除，为下面更新数据做准备
        self.table_widget.clear()
        current_row_count = self.table_widget.rowCount()
        self.table_widget.clearContents()

        for result in cms_result:
            # print(i)
            for row_list in result:
                self.table_widget.insertRow(current_row_count)
                # 写入数据
                for i, ele in enumerate(row_list):
                    cell = QTableWidgetItem(str(ele))
                    cell.setToolTip(str(ele))
                    # 表格内容不能被修改
                    if i in [0, 1, 2, 3, 4, 5]:
                        cell.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    self.table_widget.setItem(current_row_count, i, cell)
                current_row_count += 1
        pass




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.setStyleSheet(qdarkstyle.load_stylesheet())


    window.show()

    sys.exit(app.exec_())