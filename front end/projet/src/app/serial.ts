import { Users } from "./users";

export interface Serial {
    id: number;
    serial_number: string;
    creater: Users;
    editor: Users;
    created_at: string;
    updated_at: string;
  }