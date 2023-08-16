import { Products } from "./products";
import { Serial } from "./serial";
import{Users} from "./users"
export interface KeyCSR {

    id: number;
    product: Products;
    serial:Serial;
    creater: Users;
    editor: Users;
    country: string;
    state: string;
    locality: string;
    organization: string;
    org_unit: string;
    common_name: string;
    // add other properties here as needed
  }
  