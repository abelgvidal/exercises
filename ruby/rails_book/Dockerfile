FROM ruby:2.4.2-alpine3.6

RUN set -ex \
    && buildDeps=' \
        build-base \
	mysql-dev \
        nodejs \
	tzdata \
	' \
    && apk update \
    && apk add  $buildDeps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY demo/Gemfile* ./
RUN bundle install --system
COPY . .

EXPOSE 3000
CMD ["rails", "server", "-b", "0.0.0.0"]
