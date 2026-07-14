FROM jekyll/jekyll:4

WORKDIR /jekyll

COPY src/Gemfile src/Gemfile.lock ./
RUN bundle install

EXPOSE 4000 35729

CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0", "--livereload", "--livereload-port", "35729", "--force_polling"]
