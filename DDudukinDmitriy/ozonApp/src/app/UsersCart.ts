export interface CheckOutData{
  countProducts: number;
  id: number;
  is_checkout: boolean;
  purchase: UsersCart[];
  totalPrice: number;
  totalWeight: number;
}
export interface UsersCart{
 count: number;
 id: number;
 price: number;
 product: any;
 weight: number;
}
