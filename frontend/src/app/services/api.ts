import axios from "axios";

import {
  API_URL
} from "@/src/lib/config";

export const api = axios.create({
  baseURL: `${API_URL}`,
});