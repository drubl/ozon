export class Product {
  id: number;
  firstPhoto: string;
  title: string;
  price: string | number;
  singleLink: string;
  description: string;
}
export class Products {
  id: number;
  product: Product;
  count: number;
  price: number;
  weight: number;
}
