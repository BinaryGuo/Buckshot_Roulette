import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="Buckshot_Roulette",  # 模块名称
    version="1.0",  # 当前版本
    author="GQX",  # 作者
    author_email="kill114514251@outlook.com",  # 作者邮箱
    description="模仿steam游戏“恶魔轮盘”，目前没有提供开发接口（只能单纯玩）",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/wupeiqi/",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
        "pygame2.5.2",
    ],
    python_requires='>=3',
)