$(function(){
    // Bind the mouseover event to the form element, using event delegation
    $('form').on('mouseover', '.rating-select .btn', function(){
      $(this).removeClass('btn-default').addClass('btn-warning');
      $(this).prevAll().removeClass('btn-default').addClass('btn-warning');
      $(this).nextAll().removeClass('btn-warning').addClass('btn-default');
    });
  
    // Bind the mouseleave event to the form element, using event delegation
    $('form').on('mouseleave', '.rating-select', function(){
      var active = $(this).parent().find('.selected');
      if(active.length) {
        active.removeClass('btn-default').addClass('btn-warning');
        active.prevAll().removeClass('btn-default').addClass('btn-warning');
        active.nextAll().removeClass('btn-warning').addClass('btn-default');
      } else {
        $(this).find('.btn').removeClass('btn-warning').addClass('btn-default');
      }
    });
  
    // Bind the click event to the form element, using event delegation
    $('form').on('click', '.rating-select .btn', function(){
      console.log('Rating clicked!');
      var reviewId = $(this).closest('.review').data('review-id');
      if($(this).hasClass('selected')) {
        $('#review-' + reviewId + '-stars .selected').removeClass('selected');
        $('#review-' + reviewId + '-rating').val('');
      } else {
        $('#review-' + reviewId + '-stars .selected').removeClass('selected');
        $(this).addClass('selected');
        var rating = $(this).val();
        $('#review-' + reviewId + '-rating').val(rating);
      }
    });
  
    $('form').submit(function(event) {
        if ($(this).data('submitted') === true) {
          event.preventDefault();
        } else {
          $(this).data('submitted', true);
        }
        var rating = $('.rating-select .selected').val();
        $('input[name="rating"]').val(rating);
      });      
  
  });
  