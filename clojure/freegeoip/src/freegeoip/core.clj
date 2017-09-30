(require '[clj-http.client :as client])

(ns freegeoip.core
  (:require [clj-http.client :as client])  
  (:gen-class))

(defn get-ip-country
  [ip]
  (let [api-call (str "http://freegeoip.net/json/" ip)
        response (client/get api-call {:as :json})]
    [ip  (:body response)]))

(defn -main
  [& ips]
  (println (map get-ip-country ips)))

