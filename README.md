### 使用django-allauth进行注册登录，重置密码，邮件验证
- 用户注册
- 用户登录
- 退出登录
- 第三方auth登录(微信，微博等)
- 邮箱验证
- 登录后密码重置
- 忘记密码，邮箱发送密码重置链接

### 配置
- setting.py
    -   ```python
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'django.contrib.staticfiles',
                'django.contrib.sites', # allauth对于站点设置django.contrib.sites有依赖
                'allauth',
                'allauth.account',
                'allauth.socialaccount',
                'allauth.socialaccount.providers.github', # 第三方providers
            ]
            SITE_ID = 1
        ```
    - 设置BACKENDS并提供用户登录验证的方法和用户登录后跳转的链接,通过email或者用户名登录
    
        ```python
            # 基本设定
            ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
            ACCOUNT_EMAIL_REQUIRED = True
            LOGIN_REDIRECT_URL = '/accounts/profile/' # 用户登录和注册后自动跳转的页面
            
            AUTHENTICATION_BACKENDS = (
                'django.contrib.auth.backends.ModelBackend',
                'allauth.account.auth_backends.AuthenticationBackend',
            )
            
            # 邮箱设定
            
            EMAIL_HOST = 'smtp.126.com'
            EMAIL_PORT = 25
            EMAIL_HOST_USER = 'haijun0427@126.com'
            '''
            新注册邮箱会报错 smtplib.SMTPAuthenticationError: (535, b'Error: authentication failed'),可以用授权码代替密码
            '''
            EMAIL_HOST_PASSWORD = 'xy0407a'
            EMAIL_USE_TLS = True
            EMAIL_FROM = 'haijun0427@126.com'
        ```
- urls.py
    ```python
        from django.conf.urls import url, include
        from django.contrib import admin
        
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url('accounts/', include('allauth.urls')),
        ]

    ```
- 设置admin后台默认网址为127.0.0.1:8000,就可以访问django_allauth所有内置的URLs

    - django-allauth内置的URLs及视图

        下面是django_allauth所有内置的URLs，均可以访问的。
        
        127.0.0.1:8000/accounts/login/（URL名account_login): 登录
        
        /accounts/signup/ (URL名account_signup): 注册
        
        /accounts/password/reset/(URL名: account_reset_password) ：重置密码
        
        /accounts/logout/ (URL名account_logout): 退出登录
        
        /accounts/password/set/ (URL名:account_set_password): 设置密码 
        
        /accounts/password/change/ (URL名: account_change_password): 改变密码（需登录）
        
        /accounts/email/(URL名: account_email) 用户可以添加和移除email，并验证
        
        /accounts/social/connections/（URL名:socialaccount_connections): 管理第三方账户

### django-allauth常见设置选项
你也可以添加其它设置选项来实现你所想要的功能， 比如设置邮件确认过期时间，限制用户使用错误密码登录的持续时间。
ACCOUNT_AUTHENTICATION_METHOD (="username" | "email" | "username_email")：指定要使用的登录方法（用户名、电子邮件地址或两者之一）

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS (=3)：邮件确认邮件的截止日期(天数)

ACCOUNT_EMAIL_VERIFICATION (="optional")：注册中邮件验证方法:“强制（mandatory）”,“可选（optional）”或“否（none）”之一

ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN (=180)：邮件发送后的冷却时间(以秒为单位)

ACCOUNT_LOGIN_ATTEMPTS_LIMIT (=5)：登录尝试失败的次数

ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT (=300)：从上次失败的登录尝试，用户被禁止尝试登录的持续时间

ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION (=False)：更改为True，用户一旦确认他们的电子邮件地址，就会自动登录

ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE (=False)：更改或设置密码后是否自动退出

ACCOUNT_LOGIN_ON_PASSWORD_RESET (=False)：更改为True，用户将在重置密码后自动登录

ACCOUNT_SESSION_REMEMBER (=None)：控制会话的生命周期，可选项还有:False,True

ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE (=False):用户注册时是否需要输入邮箱两遍

ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE (=True): 用户注册时是否需要用户输入两遍密码

ACCOUNT_USERNAME_BLACKLIST (=[]):用户不能使用的用户名列表

ACCOUNT_UNIQUE_EMAIL (=True)： 加强电子邮件地址的唯一性

ACCOUNT_USERNAME_MIN_LENGTH (=1)：用户名允许的最小长度的整数

SOCIALACCOUNT_AUTO_SIGNUP (=True)：使用从社会帐户提供者检索的字段(如用户名、邮件)来绕过注册表单

LOGIN_REDIRECT_URL (="/") 设置登录后跳转链接

ACCOUNT_LOGOUT_REDIRECT_URL (="/") 设置退出登录后跳转链接


### 扩展
- 127.0.0.0:8000/accounts/profile 这个链接暂时还不能访问，因为django-allauth没有提供用户资料的修改功能和用户资料的扩展功能
- 创建user扩展app 例如users
    ```python
        # setting.py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'users.apps.UsersConfig',  # 扩展用户
            'django.contrib.sites',  # allauth对于站点设置django.contrib.sites有依赖
            'allauth',
            'allauth.account',
            'allauth.socialaccount',
            'allauth.socialaccount.providers.github'

        ]
        # urls.py 
        from django.conf.urls import url, include
        from django.contrib import admin
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'accounts/', include('allauth.urls')),
            url(r'accounts/', include('users.urls')),
        ]
    ```
    
- 用户更新资料需要用到表单，所以我们把表单单独放在forms.py,创建了两个表单：一个是更新用户资料时使用，一个是重写用户登录表单。
  - 为什么我们需要重写用户登录表单？因为django-allauth在用户注册只会创建User对象，不会创建与之关联的UserProfile对象，我们希望用户在注册时两个对象一起被创建，并存储到数据库中。这点非常重要。通过重写表单，你还可以很容易添加其它字段。
    ```python
        from django import forms
        from .models import UserProfile
        
        
        class ProfileForm(forms.Form):
            first_name = forms.CharField(label='名', max_length=50, required=False)
            last_name = forms.CharField(label='姓', max_length=50, required=False)
            org = forms.CharField(label='机构', max_length=50, required=False)
            telephone = forms.CharField(label='电话', max_length=50, required=False)
        
        
        class SignupForm(forms.Form):
            def signup(self, request, user):
                user_profile = UserProfile()
                user_profile.user = user
                user.save()
                user_profile.save()
    ```
  - 要告诉django-allauth使用我们自定义的登录表单，我们只需要在settings.py里加入一行。
    ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'