import { Users } from "./users";

export interface Products {
    [x: string]: any;
    id:number;
    product_code:string;
    typer:string;
    designation:string;
    creater: {
        username: string;
      };
    editor: Users;
    created_at: string;
    updated_at: string; 
}