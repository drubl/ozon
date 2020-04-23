import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {Product} from '../product';
import {ProductService} from "../product.service";
import {Observable, Subject, Subscription} from 'rxjs';
import {ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-page-search',
  templateUrl: './page-search.component.html',
  styleUrls: ['./page-search.component.css']
})
export class PageSearchComponent implements OnInit {

  productsOnPage$: Product[] = [];
  private searchTerms = new Subject<string>();
  nameSearch: string;
  toggleSearchInfo = false;
  info: any;
  constructor(private productService: ProductService, private route: ActivatedRoute) {
  }
  showSearchItems($event: string) {
    this.searchTerms.next($event);
    this.nameSearch = $event;
    this.productService.searchProducts($event).subscribe(value => {
      this.productsOnPage$ = value;
      this.toggleSearchInfo = true;
    });
  }
  ngOnInit(): void {
  }

}
