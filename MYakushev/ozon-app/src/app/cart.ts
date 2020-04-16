import {Product, Products} from './product';


export class Cart {
  countPurchase: number;
  id: number;
  is_checkout: boolean;
  purchase: Products[];
  totalPrice: number;
  totalWeight: number;
}
