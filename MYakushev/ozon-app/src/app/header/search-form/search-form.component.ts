import {Component, OnInit, Output, EventEmitter} from '@angular/core';
import {Observable, Subject, Subscription} from 'rxjs';
import {ProductService, SearchProducts} from '../../product.service';
import {Product} from '../../product';
import { debounceTime, distinctUntilChanged, switchMap} from 'rxjs/operators';
import {ActivatedRoute, Router} from '@angular/router';
import {Auth} from "../../auth";


@Component({
  selector: 'app-search-form',
  templateUrl: './search-form.component.html',
  styleUrls: ['./search-form.component.css']
})
export class SearchFormComponent implements OnInit {
  @Output() onClickSearchButton: EventEmitter<string> = new EventEmitter<string>();
  products$: Observable<Product[]>;
  private searchTerms = new Subject<string>();
  private routeSubscription: Subscription;
  private searchTitleSubmit;
  constructor(public productService: ProductService, private router: Router, private auth: Auth, private route: ActivatedRoute) { }
  search(title: string): void {
    this.searchTerms.next(title);
  }
  ngOnInit(): void {
    this.routeSubscription = this.route.params.subscribe(params => {
      this.searchTitleSubmit = params['search'];
      if (this.searchTitleSubmit === undefined) {
        return;
      } else {
        this.getSearchProducts(this.searchTitleSubmit);
      }
    });
  }
  getSearchProducts() {
    this.productService.searchProducts(this.searchTitleSubmit).subscribe(answer => {
      console.log('answer', answer);
      this.onClickSearchButton.emit(this.searchTitleSubmit);
    });
  }

  searchButtonClick($event: Event, value: string, searchBox: HTMLInputElement) {
    $event.preventDefault();
    this.router.navigate(['/search', { search: value }]);
    this.onClickSearchButton.emit(value);
    searchBox.value = '';
  }
}
