<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        
        <xsl:variable name="identifier" select="large-textbox/identifier" />
        
        <div class="container mt-2">
            <div class="form-group">
                
                <label for="{$identifier}">
                    <xsl:value-of select="large-textbox/label"/> 
                </label>
                
                <textarea class="form-control form-control-sm" 
                          id="{$identifier}" name="{$identifier}">
                </textarea>
                
                <small class="form-text form-text-sm text-muted">
                    <xsl:value-of select="large-textbox/tooltip"/>
                </small>
                
            </div>
        </div>
        
    </xsl:template>
</xsl:stylesheet>
