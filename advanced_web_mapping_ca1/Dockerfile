FROM continuumio/miniconda3

LABEL maintainer="Bujar Raufi"

# 设置项目环境变量
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=advanced_web_mapping_ca1.settings

RUN mkdir -p /app
WORKDIR /app

# 创建 Conda 环境
COPY ENV.yml .
RUN conda env create -f ENV.yml

# 使用新环境运行命令
SHELL ["conda", "run", "-n", "awm_env", "/bin/bash", "-c"]

# 将 Django 项目文件复制到镜像中
COPY . /app
ENV PYTHONPATH="/app"

# The code to run when container is started:
COPY manage.py .
ENTRYPOINT ["conda", "run", "-n", "awm_env"]

# 暴露端口
EXPOSE 8001

# 启动服务器
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
