import xadmin
from xadmin import views

class BaseSetting(object):
    """xadmin的基本配置"""
    enable_themes = True  # 开启主题切换功能
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView, BaseSetting)

class GlobalSettings(object):
    """xadmin的全局配置"""
    site_title = "CoderCC 博客"  # 设置站点标题
    site_footer = "CoderCC & 程序员cc"  # 设置站点的页脚
    menu_style = "accordion"  # 设置菜单折叠

xadmin.site.register(views.CommAdminView, GlobalSettings)

# 轮播图
from .models import Banner
class BannerInfoModelAdmin(object):
    list_display=["title","orders","is_show"]
xadmin.site.register(Banner, BannerInfoModelAdmin)