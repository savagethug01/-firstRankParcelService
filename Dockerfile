FROM python:3.11-slim

WORKDIR /app

# Copy your app source
COPY ./shipping_site /app

# ✅ Copy build.sh and entrypoint.sh into the image
COPY build.sh /app/build.sh
COPY entrypoint.sh /app/entrypoint.sh

# ✅ Make sure the scripts are executable and run the build
RUN chmod +x build.sh && ./build.sh
RUN chmod +x entrypoint.sh

EXPOSE 8000

CMD ["./entrypoint.sh"]
